import dash
import os
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import pages.home as home
import pages.dashboard as dashboard
import pages.report as report

# Initialisation de l'app
app = dash.Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="Global Quality Insights"
)

server = app.server  # Pour Railway

# Store pour mémoriser la langue sélectionnée
language_store = dcc.Store(id='language-store', data='fr')

# Barre de navigation
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dcc.Link("Accueil", href="/", className="nav-link")),
        dbc.NavItem(dcc.Link("Analyse", href="/dashboard", className="nav-link")),
        dbc.NavItem(dcc.Link("Documentation", href="/report", className="nav-link")),
        dbc.Button("EN/FR", id="language-toggle", color="secondary", outline=True, className="ms-2"),
    ],
    brand="Global Quality Insights",
    brand_href="/",
    color="dark",
    dark=True,
    className="mb-4"
)

# Layout global
app.layout = html.Div([
    dcc.Location(id='url'),
    language_store,
    navbar,
    html.Div(id='page-content')
])

# Callback pour le bouton de langue
@app.callback(
    Output('language-store', 'data'),
    Input('language-toggle', 'n_clicks'),
    State('language-store', 'data'),
    prevent_initial_call=True
)
def switch_language(n_clicks, current_lang):
    return 'en' if current_lang == 'fr' else 'fr'

# Callback de navigation
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname'),
     Input('language-store', 'data')]
)
def display_page(pathname, lang):
    if pathname == "/dashboard":
        return dashboard.layout(lang)
    elif pathname == "/report":
        return report.layout(lang)
    else:
        return home.layout(lang)

# Import et enregistrement des callbacks globaux
import callbacks
callbacks.register_callbacks(app)

# Lancement de l'application
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(
        host="0.0.0.0",
        port=port,
        debug=False,
        use_reloader=False
    )
