from dash import html, dcc
import dash_bootstrap_components as dbc

def layout(lang='fr'):
    return dbc.Container([
        html.H1("Analyse interactive" if lang == 'fr' else "Interactive Dashboard", className="text-success my-4"),

        html.P(
            "Comparer visuellement le nombre de tickets qualité selon leur gravité et leur répartition par site."
            if lang == 'fr' else
            "Visually compare the number of quality tickets by severity and their distribution across sites."
        ),

        # 🧩 Filtres côte à côte et centrés
        dbc.Row([
            dbc.Col([
                html.Label("Filtrer par pays" if lang == 'fr' else "Filter by country",
                           style={"whiteSpace": "nowrap"}),
                dcc.Dropdown(
                    id="dropdown-pays",
                    options=[
                        {"label": "France", "value": "France"},
                        {"label": "USA", "value": "USA"},
                        {"label": "Allemagne" if lang == 'fr' else "Germany", "value": "Germany"},
                    ],
                    multi=True,
                    placeholder="Sélectionnez un ou plusieurs pays" if lang == 'fr' else "Select one or more countries"
                ),
            ], md="auto", className="text-center"),

            dbc.Col([
                html.Label("Filtrer par gravité" if lang == 'fr' else "Filter by severity",
                           style={"whiteSpace": "nowrap"}),
                dcc.Dropdown(
                    id="dropdown-priorite",
                    options=[
                        {"label": "Mineur" if lang == 'fr' else "Minor", "value": "mineure"},
                        {"label": "Majeur" if lang == 'fr' else "Major", "value": "majeure"},
                        {"label": "Critique" if lang == 'fr' else "Critical", "value": "critique"},
                    ],
                    multi=True,
                    placeholder="Sélectionnez un niveau" if lang == 'fr' else "Select severity"
                ),
            ], md="auto", className="text-center"),
        ], justify="center", className="mb-4"),

        # 📊 Graphiques côte à côte
        dbc.Row([
            dbc.Col(dcc.Graph(id="graph-top-defauts", figure={"data": [], "layout": {"title": "Top défauts"}}), md=6),
            dbc.Col(dcc.Graph(id="graph-defauts-par-pays", figure={"data": [], "layout": {"title": "Défauts par pays"}}), md=6),
        ]),

        # 📈 Intégration Power BI
        html.Hr(),

        html.H3("Visualisation CODIR Monde" if lang == 'fr' else "Global CODIR View", className="mt-4"),
        html.Iframe(
            src="https://app.powerbi.com/view?r=eyJrIjoiZGQ2NWM5MjYtZTUwNC00N2UzLWFlMGQtMzA4MjhjMGViZmVkIiwidCI6IjllNTI3MWNjLWFkOTAtNDUyZC1hNTRhLWQyMDY3MTFiYWQ5MSJ9&pageName=397332d339335a2a37bf",
            style={"width": "100%", "height": "500px", "border": "none"}
        ),

        html.H3("Visualisation Site France" if lang == 'fr' else "France Site View", className="mt-4"),
        html.Iframe(
            src="https://app.powerbi.com/view?r=eyJrIjoiOTM3MDNhZWEtNDcxNy00YmExLWIwMjktN2FhMDgzZmZmMTJlIiwidCI6IjllNTI3MWNjLWFkOTAtNDUyZC1hNTRhLWQyMDY3MTFiYWQ5MSJ9&pageName=397332d339335a2a37bf",
            style={"width": "100%", "height": "500px", "border": "none"}
        ),

        html.H3("Visualisation Site Allemagne" if lang == 'fr' else "Germany Site View", className="mt-4"),
        html.Iframe(
            src="https://app.powerbi.com/view?r=eyJrIjoiODE1MDg5NTMtYThmYy00OTZmLTljODgtNmRmNDQ5ZjNmMTI2IiwidCI6IjllNTI3MWNjLWFkOTAtNDUyZC1hNTRhLWQyMDY3MTFiYWQ5MSJ9&pageName=397332d339335a2a37bf",
            style={"width": "100%", "height": "500px", "border": "none"}
        ),

        html.H3("Visualisation Site USA" if lang == 'fr' else "USA Site View", className="mt-4"),
        html.Iframe(
            src="https://app.powerbi.com/view?r=eyJrIjoiZWQxNWY1ZjEtMzQwMC00OTY5LWI1NGEtZTk2MjQ1YTcwYWRmIiwidCI6IjllNTI3MWNjLWFkOTAtNDUyZC1hNTRhLWQyMDY3MTFiYWQ5MSJ9&pageName=397332d339335a2a37bf",
            style={"width": "100%", "height": "500px", "border": "none"}
        ),
    ], className="mb-5")
