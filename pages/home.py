from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_player as dp


def layout(lang='fr'):
    return html.Div([
        html.H1("Global Quality Insights", className="text-primary my-4"),

        dbc.Row([
            dbc.Col([
                html.H3("Contexte du projet" if lang == 'fr' else "Project Context"),
                html.P(
                    "L’année 2023 a marqué un tournant stratégique pour l’entreprise HealthCare, acteur majeur de l’industrie pharmaceutique. Déjà implantée en France avec deux sites de production à Lyon et Grenoble, l’entreprise a renforcé sa présence internationale en procédant à l’acquisition de cinq nouveaux sites :" if lang == 'fr' else
                    "The year 2023 marked a strategic turning point for HealthCare, a major player in the pharmaceutical industry. Already established in France with two production sites in Lyon and Grenoble, the company expanded its global presence by acquiring five new sites:"
                ),
                html.Ul([
                    html.Li("Trois sites en Allemagne : Munich, Düsseldorf, Berlin" if lang == 'fr' else "Three sites in Germany: Munich, Düsseldorf, Berlin"),
                    html.Li("Deux sites aux États-Unis : Boston, Chicago" if lang == 'fr' else "Two sites in the United States: Boston, Chicago"),
                ]),
                html.P(
                    "Cette expansion visait à renforcer la capacité de production à l’échelle mondiale tout en rapprochant les unités de fabrication des marchés locaux. [...]" if lang == 'fr' else
                    "This expansion aimed to strengthen global production capacity while bringing manufacturing units closer to local markets. [...]"
                ),

                html.H3("Objectifs" if lang == 'fr' else "Objectives"),
                html.Ul([
                    html.Li(text) for text in ([
                        "Unifier et nettoyer les données multilingues liées aux incidents qualité.",
                        "Analyser les défauts par ligne de production, type d’erreur et gravité.",
                        "Visualiser les données dans un tableau de bord interactif.",
                        "Fournir un rapport synthétique pour faciliter la prise de décision.",
                        "Faciliter la collaboration entre les équipes internationales via Jira et Confluence."
                    ] if lang == 'fr' else [
                        "Unify and clean multilingual data related to quality incidents",
                        "Analyze defects by production line, error type, and severity",
                        "Visualize the data through an interactive dashboard",
                        "Deliver a concise report to support decision-making",
                        "Facilitate collaboration via Jira and Confluence integration"
                    ])
                ]),

                html.Div([
                    html.Div(
                        dp.DashPlayer(
                            url="https://youtu.be/4A2vZKA4Amk",
                            controls=True,
                            playing=False,
                            style={"width": "100%", "aspectRatio": "16 / 9"}
                        ),
                        className="video-container"
                    )
                ], className="video-section"),

                html.Br(),
                html.P("Ci-dessous, une représentation du processus de gestion des tickets qualité, de leur ouverture à leur clôture." if lang == 'fr' else "Below is a visual representation of the quality ticket handling process, from creation to closure."),
                html.Br(),

                html.H3("📈 Visualisation du processus qualité (workflow)" if lang == 'fr' else "📈 Quality Workflow Overview"),

                html.Iframe(
                    srcDoc="""
                    <script type=\"module\">
                      import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
                      mermaid.initialize({ startOnLoad: true });
                    </script>
                    <div class=\"mermaid\">
                    graph LR
                        Start(Démarré: 148 tickets)
                        Todo(À faire: 36 tickets)
                        Progress(En cours: 112 tickets)
                        Analyse(Analyse: 18 tickets)
                        Blocked(Bloqué: 10 tickets)
                        Done(Clôturé: 64 tickets)

                        Start --> Todo
                        Start --> Progress
                        Progress --> Analyse
                        Progress --> Blocked
                        Progress --> Done
                    </div>
                    """,
                    width="100%",
                    height="500",
                    style={"border": "none"}
                ),
            ])
        ])
    ], className="px-4")
