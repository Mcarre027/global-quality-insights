print("📦 Chargement de callbacks.py")
from dash import Input, Output
import plotly.express as px
import pandas as pd

def register_callbacks(app):
    # Chargement et nettoyage du CSV
    print("📄 Lecture du fichier CSV...")
    df_raw = pd.read_csv("assets/tickets_clean.csv", encoding='latin1')

    for col in ['Type_incident', 'Site', 'Priorite']:
        df_raw[col] = df_raw[col].astype(str).str.encode('latin1', errors='ignore').str.decode('utf-8', errors='ignore')
        df_raw[col] = df_raw[col].str.strip().str.lower()

    # Extraction pays (à partir du site)
    df_raw['Pays'] = df_raw['Site'].apply(
        lambda x: 'france' if 'france' in x else
                  'germany' if 'germany' in x else
                  'usa' if 'usa' in x else 'autre'
    )

    @app.callback(
        Output("graph-top-defauts", "figure"),
        Output("graph-defauts-par-pays", "figure"),
        Input("language-store", "data"),
        Input("dropdown-pays", "value"),
        Input("dropdown-priorite", "value"),
    )
    def update_graphs(lang, selected_pays, selected_priorite):
        dff = df_raw.copy()

        # Harmonisation des valeurs des filtres
        pays_mapping = {'France': 'france', 'Germany': 'germany', 'USA': 'usa'}
        priorite_mapping = {
            'Minor': 'mineure', 'Major': 'majeure', 'Critical': 'critique',
            'Mineur': 'mineure', 'Majeur': 'majeure', 'Critique': 'critique'
        }

        if selected_pays:
            selected_pays = [pays_mapping.get(p, p).lower() for p in selected_pays]
            dff = dff[dff['Pays'].isin(selected_pays)]

        if selected_priorite:
            selected_priorite = [priorite_mapping.get(p, p).lower() for p in selected_priorite]
            dff = dff[dff['Priorite'].isin(selected_priorite)]

        print(f"📊 Filtres appliqués – Lang: {lang}, Pays: {selected_pays}, Priorité: {selected_priorite}")
        print(f"📊 Taille du dataframe filtré : {len(dff)} lignes")

        # Graphique 1 – Top 10 types d'incident
        top_defauts = dff['Type_incident'].value_counts().nlargest(10).reset_index()
        top_defauts.columns = ['Type_incident', 'Count']
        title1 = "Top 10 des défauts qualité" if lang == 'fr' else "Top 10 Quality Issues"
        fig1 = px.bar(top_defauts, x='Type_incident', y='Count', title=title1, text='Count')
        fig1.update_layout(xaxis_title=None, yaxis_title=None, xaxis_tickangle=-45)

        # Graphique 2 – Tickets par site
        by_site = dff['Site'].value_counts().reset_index()
        by_site.columns = ['Site', 'Nombre_tickets']
        title2 = "Répartition des tickets par site" if lang == 'fr' else "Tickets per Site"
        fig2 = px.bar(by_site, x="Site", y="Nombre_tickets", title=title2, text='Nombre_tickets')
        fig2.update_layout(xaxis_title=None, yaxis_title=None, xaxis_tickangle=-45)

        return fig1, fig2
