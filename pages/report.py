from dash import html
import dash_bootstrap_components as dbc

def layout(lang='fr'):
    if lang == 'en':
        return dbc.Container([
            html.H1("Documentation & Reports", className="text-warning my-4"),

            html.P("This page gathers useful links to documentation, quality reports, and Jira tickets related to the project."),

            html.H3("\U0001F4C2 Project Documentation Access"),
            html.Ul([
                html.Li(html.A("Confluence – Project Summary", href="https://confluence.external-share.com/content/9e9299c5-4122-41bd-bedb-41a1d49f67aa", target="_blank")),
                html.Li(html.A("PDF – Quality Report", href="https://drive.google.com/file/d/1rWB1_UTUA2qim1tyFEEFga7qJ16HMQGU/view?usp=sharing", target="_blank")),
            ]),

            html.Div(style={"height": "20px"}),
            html.H3("\U0001F4CA Power BI Dashboards"),
            html.Ul([
                html.Li(html.A("Global Codir Dashboard", href="https://app.powerbi.com/reportEmbed?reportId=275890d5-8263-49ab-8ee5-dc261e5a007b&appId=f8ec4fbb-e3e7-4d1e-8363-1f75da55f38e&autoAuth=true&ctid=9e5271cc-ad90-452d-a54a-d206711bad91", target="_blank")),
                html.Li(html.A("France Site Dashboard", href="https://app.powerbi.com/reportEmbed?reportId=053eba33-4c3b-440c-be6c-30cab8a38a18&appId=5dba965d-66c6-4b67-9f0d-3a81a4d0baf9&autoAuth=true&ctid=9e5271cc-ad90-452d-a54a-d206711bad91", target="_blank")),
                html.Li(html.A("Germany Site Dashboard", href="https://app.powerbi.com/reportEmbed?reportId=1e7514ab-1979-4b34-97bd-02621a3cd7c6&appId=b40e9bbc-b1c8-47c4-b163-ea46088ecad7&autoAuth=true&ctid=9e5271cc-ad90-452d-a54a-d206711bad91", target="_blank")),
                html.Li(html.A("USA Site Dashboard", href="https://app.powerbi.com/reportEmbed?reportId=7509934f-6e6e-42ab-bb5f-fccff3891580&appId=d20891c9-f1b9-4124-a1a8-ec24ae6328d4&autoAuth=true&ctid=9e5271cc-ad90-452d-a54a-d206711bad91", target="_blank")),
            ]),

            html.Div(style={"height": "20px"}),
            html.H3("\U0001F4D8 Confluence – Quality Procedure"),
            html.Ul([
                html.Li(html.A("Procedure – Data Cleaning & Preparation", href="https://confluence.external-share.com/content/c75b6fdd-17fa-4971-987c-d1761a705214", target="_blank")),
                html.Li(html.A("User Documentation – Dashboard", href="https://confluence.external-share.com/content/f50418fa-ebaa-457b-8222-f21e1c9dbc6a", target="_blank")),
                html.Li(html.A("Quality Procedure – Format Change Packaging Line (100 ml → 250 ml)", href="https://confluence.external-share.com/content/729763/external_share_link", target="_blank")),
            ]),

            html.Div(style={"height": "20px"}),
            html.Div(style={"height": "20px"}),
            html.H3("\U0001F4CB Jira Tickets (sample)"),
            dbc.Table([
                html.Thead(html.Tr([html.Th("Ticket"), html.Th("Status"), html.Th("Country"), html.Th("Severity")])),
                html.Tbody([
                    html.Tr([html.Td("QAL-123"), html.Td("Resolved"), html.Td("France"), html.Td("Major")]),
                    html.Tr([html.Td("QAL-456"), html.Td("In progress"), html.Td("USA"), html.Td("Critical")]),
                    html.Tr([html.Td("QAL-789"), html.Td("Closed"), html.Td("Germany"), html.Td("Minor")]),
                ])
            ], bordered=True, hover=True, responsive=True, striped=True),

            html.Br(),
            html.H3("\U0001F4CA Jira Dashboard View"),
            html.Ul([
                html.Li(html.A("Access Jira dashboard", href="https://jira.external-share.com/issue/445bc81f-d915-4fca-b44f-d49408bc0787", target="_blank")),
            ]),

            html.Div(style={"height": "20px"}),
            html.Div(style={"height": "20px"}),
            html.H3("\U0001F50D Filters and Jira Ticket Table"),
            html.H4("\u2699\ufe0f Jira Filters"),
            html.Div(style={"height": "20px"}),
            html.Ul([
                html.Li(html.A("To-do Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10152&atlOrigin=eyJpIjoiZDU2ZTA3N2I1ZTVmNDAwYjlkZmI1MGZjNThiMGFjNTYiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Closed Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10153&atlOrigin=eyJpIjoiMDY4NGE3YzI5YjYzNDQ3OGIyYzRjZWQzMzg3YzUzODciLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("In-progress Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10066&atlOrigin=eyJpIjoiY2FiNWM5ZThhNzBkNDRjNzkxMjA2YWFhNzkzYWMyN2EiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Matthieu's Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10132&atlOrigin=eyJpIjoiNTQzMzUxMzk1MDM2NGRiMWI5ZTk1NDc1MTllYjY4NmQiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Lisa's Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10143&atlOrigin=eyJpIjoiN2M4ZmUwN2ZkM2VhNDJkNWI2MDNhMmUzYzQ4YmU3MzYiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Stefan's Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10145&atlOrigin=eyJpIjoiOGViMzBlMTA0MzYyNDdhMmEzMTZmZWY0MDU3MTBiY2IiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Jack's Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10144&atlOrigin=eyJpIjoiNzdlMjhmMWIzMzY5NDRhM2E1NDdjZTczNzQwNDZkNTYiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("France Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10140&atlOrigin=eyJpIjoiNDNhOWI1Yjk2MWM5NDU1OThjYjUyOGQ4MGE1ZDg1YjYiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Germany Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10141&atlOrigin=eyJpIjoiZDY3OTNkNzVjODc0NDViN2ExMTlmYTE2ZWYwOGQ3ZjkiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("USA Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10142&atlOrigin=eyJpIjoiMWRhMWZjMTBmZmE5NDYzYzk2MDIxNDRjOWIzMjVmYTUiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Lyon Site Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10134&atlOrigin=eyJpIjoiMDgxNDY1YjhlMTViNGFkYTlmNzBkNmMwNDY1Nzk0ODgiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Grenoble Site Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10133&atlOrigin=eyJpIjoiZjE5YWEwN2Y3YmU3NDVhM2IyZDA4ZGY1ZDdkOWVjNzAiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Berlin Site Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10136&atlOrigin=eyJpIjoiYzM5OWNmMzhiMjJjNDIzNDk2YTU4MjZlYmI0NGIxNTEiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Düsseldorf Site Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10135&atlOrigin=eyJpIjoiZTVmZjgwNzhhNGI4NDNkOGI4N2E0Y2ZjMTliM2U4N2UiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Munich Site Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10137&atlOrigin=eyJpIjoiNWU5ZDFiOWJlMDJlNDg4N2I1ZGNhYTZkOTdlYTIzNTMiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Boston Site Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10138&atlOrigin=eyJpIjoiMTBiNjJiN2E4MTcwNGY4OWJkNjc4MTU0ODI4MmViMGMiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Chicago Site Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10139&atlOrigin=eyJpIjoiZmVhOTMyYjYxZjJiNGQ0OTg0OTQxM2UxYmI2YTZmZWEiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Line A1 Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10166&atlOrigin=eyJpIjoiYjk2ODUxYWE5MzM0NDA1YWExMmM2MDY5MzZkZmE0ZDQiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Line B2 Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10167&atlOrigin=eyJpIjoiZTI2NGE4ZmFjMzQ4NDA1MGE0ODhmNGU5YzAwMzEyMjEiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Line C4 Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10168&atlOrigin=eyJpIjoiZDg2ZGVhMDUyMGQ5NGM3NWJjMTQ4MmIyOWE0NTBhN2IiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Line 7 Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10169&atlOrigin=eyJpIjoiMmUxNGMzNjM5NmNkNDRmY2E4NTExMmRiZTI2NTc0MWUiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Line 4 Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10170&atlOrigin=eyJpIjoiYjIxMjA0YTJjZGQ1NDlkMDk1NDRlYzc4MDE2ZGEyYjYiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Line 7 Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10171&atlOrigin=eyJpIjoiZDllY2FhYmFhZWFmNGY5MGFiYTUwMzcyMzg4ZjI0YzQiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Linie 2 Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10172&atlOrigin=eyJpIjoiMDYyMmQ5MDU4OWM0NGEzNTk4NjRkMzBmMjM3YWUxMWIiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Linie 3 Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10173&atlOrigin=eyJpIjoiNTJlOWNkMThjMzc1NDA1NmI0YTVmOTZhZTdlOTAyYjIiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Linie 5 Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10174&atlOrigin=eyJpIjoiY2JlMzk2YmQ0ODEwNDJmN2ExNjEwNjJkZDIwZGMzMjciLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("AMOX250C Product Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10175&atlOrigin=eyJpIjoiNDhiY2M2NDQ0OTgzNGYyNDg0MTFmODMyZGEzOTlkYTgiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("AMOX500 Product Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10176&atlOrigin=eyJpIjoiNjllNDAxMTJmZTZkNGRkY2IxOGQ3OWY3ODIxYTJkMzYiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("IBUPRO400 Product Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10177&atlOrigin=eyJpIjoiM2JlZDk4ZTBlYmY3NDZlZGE2ZmNlZDBjY2YyMTRhYTMiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("IBUPRO200 Product Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10178&atlOrigin=eyJpIjoiZGZkNGFmZWZjNmNiNDA0ZWI1MjkyZGIwMDAyYTc4ZTUiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A(" IBUPRO400 Product Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10179&atlOrigin=eyJpIjoiMzhiMGI4NThiNTA5NGRiMjkxNzZhMGIxZGY2ZTlkMjEiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("PARA500MG Product Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10180&atlOrigin=eyJpIjoiMmJkODNlODRjOWRiNGQ1YmFhY2M2YmY1NWQ3MTE5ODgiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("VACCINX Product Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10181&atlOrigin=eyJpIjoiODc4MmUxNmFkMGJlNGZhNmJkYWJhNjlhOWYxMGU0YmYiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("VITD1000 Product Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10182&atlOrigin=eyJpIjoiOGRlNjAwZDlmYjEyNGRhMjkyZmQyNThiZmU2M2JkYWMiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("ZINCPLUS Product Ticket", href="https://carrehomebusiness.atlassian.net/issues/?filter=10183&atlOrigin=eyJpIjoiZWJmZWE4ODllYTFjNGI5Yzk2M2ZhODcyOWRlYTk4MzIiLCJwIjoiaiJ9", target="_blank")),
            ]),

            html.Div(style={"height": "20px"}),
            html.H4("\U0001F4C4 Ticket Table View"),
            html.Div(style={"height": "20px"}),
            html.Ul([
                html.Li(html.A("Global Ticket Table", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10002", target="_blank")),
                html.Li(html.A("Matthieu's Ticket Table", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10036", target="_blank")),
                html.Li(html.A("Lisa's Ticket Table", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10034", target="_blank")),
                html.Li(html.A("Stefan's Ticket Table", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10035", target="_blank")),
                html.Li(html.A("Jack's Ticket Table", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10037", target="_blank")),
                html.Li(html.A("Line A1 Ticket Table", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10067", target="_blank")),
                html.Li(html.A("Line B2 Ticket Table", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10068", target="_blank")),
                html.Li(html.A("Line C4 Ticket Table", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10069", target="_blank")),
                html.Li(html.A("Line 2 Ticket Table", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10070", target="_blank")),
                html.Li(html.A("Line 4 Ticket Table", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10071", target="_blank")),
                html.Li(html.A("Line 7 Ticket Table", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10072", target="_blank")),
                html.Li(html.A("Linie 2 Ticket Table", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10100", target="_blank")),
                html.Li(html.A("Linie 3 Ticket Table", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10101", target="_blank")),
                html.Li(html.A("Linie 5 Ticket Table", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10102", target="_blank")),
             ]),
        ], fluid=True)

    else:
        return dbc.Container([

            html.H1("Documentation & Rapport", className="text-warning my-4"),

            html.P("Cette page centralise les liens utiles vers la documentation, les rapports qualité, et les tickets Jira liés au projet."),

            html.H3("\U0001F4C2 Accès à la documentation du projet"),
            html.Ul([
                html.Li(html.A("Confluence – Synthèse du projet", href="https://confluence.external-share.com/content/9e9299c5-4122-41bd-bedb-41a1d49f67aa", target="_blank")),
                html.Li(html.A("PDF – Rapport qualité", href="https://drive.google.com/file/d/1glk-s4jTSVRpSrcqamzCxbSP699SmndA/view?usp=sharing", target="_blank")),
            ]),

            html.Div(style={"height": "20px"}),

            html.H3("\U0001F4CA Visualisations Power BI"),
            html.Ul([
                html.Li(html.A("Visualisation Codir Monde", href="https://app.powerbi.com/reportEmbed?reportId=275890d5-8263-49ab-8ee5-dc261e5a007b&appId=f8ec4fbb-e3e7-4d1e-8363-1f75da55f38e&autoAuth=true&ctid=9e5271cc-ad90-452d-a54a-d206711bad91", target="_blank")),
                html.Li(html.A("Visualisation Site France", href="https://app.powerbi.com/reportEmbed?reportId=053eba33-4c3b-440c-be6c-30cab8a38a18&appId=5dba965d-66c6-4b67-9f0d-3a81a4d0baf9&autoAuth=true&ctid=9e5271cc-ad90-452d-a54a-d206711bad91", target="_blank")),
                html.Li(html.A("Visualisation Site Allemagne", href="https://app.powerbi.com/reportEmbed?reportId=1e7514ab-1979-4b34-97bd-02621a3cd7c6&appId=b40e9bbc-b1c8-47c4-b163-ea46088ecad7&autoAuth=true&ctid=9e5271cc-ad90-452d-a54a-d206711bad91", target="_blank")),
                html.Li(html.A("Visualisation Site USA", href="https://app.powerbi.com/reportEmbed?reportId=7509934f-6e6e-42ab-bb5f-fccff3891580&appId=d20891c9-f1b9-4124-a1a8-ec24ae6328d4&autoAuth=true&ctid=9e5271cc-ad90-452d-a54a-d206711bad91", target="_blank")),
            ]),
            html.Div(style={"height": "20px"}),

            html.H3("\U0001F4D8 Procédure qualité Confluence"),
            html.Ul([
                html.Li(html.A("Procédure – Nettoyage & Préparation des Données", href="https://confluence.external-share.com/content/c75b6fdd-17fa-4971-987c-d1761a705214", target="_blank")),
                html.Li(html.A("Documentation Utilisateur – Tableau de bord", href="https://confluence.external-share.com/content/f50418fa-ebaa-457b-8222-f21e1c9dbc6a", target="_blank")),
                html.Li(html.A("Procédure Qualité – Changement de Format Ligne de Conditionnement (100 ml → 250 ml)", href="https://confluence.external-share.com/content/729763/external_share_link", target="_blank")),
            ]),

            html.Div(style={"height": "20px"}),

            html.H3("\U0001F4CB Tickets Jira (extrait)"),
            dbc.Table([
                html.Thead(html.Tr([html.Th("Ticket"), html.Th("Statut"), html.Th("Pays"), html.Th("Gravité")])),
                html.Tbody([
                    html.Tr([html.Td("QAL-123"), html.Td("Résolu"), html.Td("France"), html.Td("Majeur")]),
                    html.Tr([html.Td("QAL-456"), html.Td("En cours"), html.Td("USA"), html.Td("Critique")]),
                    html.Tr([html.Td("QAL-789"), html.Td("Clôturé"), html.Td("Allemagne"), html.Td("Mineur")]),
                ])
            ], bordered=True, hover=True, responsive=True, striped=True),

            html.Div(style={"height": "20px"}),
            html.Div(style={"height": "20px"}),
            html.Br(),
            html.H3("\U0001F4CA Visualisation Tableau de bord Jira"),
            html.Ul([
                html.Li(html.A("Accéder au tableau Jira", href="https://jira.external-share.com/issue/445bc81f-d915-4fca-b44f-d49408bc0787", target="_blank")),
            ]),

            html.Div(style={"height": "20px"}),
            html.Div(style={"height": "20px"}),
            html.H3("\U0001F50D Filtres et tableau Jira par ticket"),
            html.Div(style={"height": "20px"}),
            html.H4("\u2699\ufe0f Filtre Jira"),
            html.Div(style={"height": "20px"}),
            html.Ul([
                html.Li(html.A("Ticket a faire", href="https://carrehomebusiness.atlassian.net/issues/?filter=10152&atlOrigin=eyJpIjoiZDU2ZTA3N2I1ZTVmNDAwYjlkZmI1MGZjNThiMGFjNTYiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket Clôturé", href="https://carrehomebusiness.atlassian.net/issues/?filter=10153&atlOrigin=eyJpIjoiMDY4NGE3YzI5YjYzNDQ3OGIyYzRjZWQzMzg3YzUzODciLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket en cours de traitement", href="https://carrehomebusiness.atlassian.net/issues/?filter=10066&atlOrigin=eyJpIjoiY2FiNWM5ZThhNzBkNDRjNzkxMjA2YWFhNzkzYWMyN2EiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket de Matthieu", href="https://carrehomebusiness.atlassian.net/issues/?filter=10132&atlOrigin=eyJpIjoiNTQzMzUxMzk1MDM2NGRiMWI5ZTk1NDc1MTllYjY4NmQiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket de Lisa", href="https://carrehomebusiness.atlassian.net/issues/?filter=10143&atlOrigin=eyJpIjoiN2M4ZmUwN2ZkM2VhNDJkNWI2MDNhMmUzYzQ4YmU3MzYiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket de Stefan", href="https://carrehomebusiness.atlassian.net/issues/?filter=10145&atlOrigin=eyJpIjoiOGViMzBlMTA0MzYyNDdhMmEzMTZmZWY0MDU3MTBiY2IiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket de Jack", href="https://carrehomebusiness.atlassian.net/issues/?filter=10144&atlOrigin=eyJpIjoiNzdlMjhmMWIzMzY5NDRhM2E1NDdjZTczNzQwNDZkNTYiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket France", href="https://carrehomebusiness.atlassian.net/issues/?filter=10140&atlOrigin=eyJpIjoiNDNhOWI1Yjk2MWM5NDU1OThjYjUyOGQ4MGE1ZDg1YjYiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket Allemagne", href="https://carrehomebusiness.atlassian.net/issues/?filter=10141&atlOrigin=eyJpIjoiZDY3OTNkNzVjODc0NDViN2ExMTlmYTE2ZWYwOGQ3ZjkiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket USA", href="https://carrehomebusiness.atlassian.net/issues/?filter=10142&atlOrigin=eyJpIjoiMWRhMWZjMTBmZmE5NDYzYzk2MDIxNDRjOWIzMjVmYTUiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket site de Lyon", href="https://carrehomebusiness.atlassian.net/issues/?filter=10134&atlOrigin=eyJpIjoiMDgxNDY1YjhlMTViNGFkYTlmNzBkNmMwNDY1Nzk0ODgiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket site de Grenoble", href="https://carrehomebusiness.atlassian.net/issues/?filter=10133&atlOrigin=eyJpIjoiZjE5YWEwN2Y3YmU3NDVhM2IyZDA4ZGY1ZDdkOWVjNzAiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket site de Berlin", href="https://carrehomebusiness.atlassian.net/issues/?filter=10136&atlOrigin=eyJpIjoiYzM5OWNmMzhiMjJjNDIzNDk2YTU4MjZlYmI0NGIxNTEiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket site de Düsseldorf", href="https://carrehomebusiness.atlassian.net/issues/?filter=10135&atlOrigin=eyJpIjoiZTVmZjgwNzhhNGI4NDNkOGI4N2E0Y2ZjMTliM2U4N2UiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket site de Munich", href="https://carrehomebusiness.atlassian.net/issues/?filter=10137&atlOrigin=eyJpIjoiNWU5ZDFiOWJlMDJlNDg4N2I1ZGNhYTZkOTdlYTIzNTMiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket site de Boston", href="https://carrehomebusiness.atlassian.net/issues/?filter=10138&atlOrigin=eyJpIjoiMTBiNjJiN2E4MTcwNGY4OWJkNjc4MTU0ODI4MmViMGMiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket site de Chicago", href="https://carrehomebusiness.atlassian.net/issues/?filter=10139&atlOrigin=eyJpIjoiZmVhOTMyYjYxZjJiNGQ0OTg0OTQxM2UxYmI2YTZmZWEiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket Ligne A1", href="https://carrehomebusiness.atlassian.net/issues/?filter=10166&atlOrigin=eyJpIjoiYjk2ODUxYWE5MzM0NDA1YWExMmM2MDY5MzZkZmE0ZDQiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket Ligne B2", href="https://carrehomebusiness.atlassian.net/issues/?filter=10167&atlOrigin=eyJpIjoiZTI2NGE4ZmFjMzQ4NDA1MGE0ODhmNGU5YzAwMzEyMjEiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket Ligne C4", href="https://carrehomebusiness.atlassian.net/issues/?filter=10168&atlOrigin=eyJpIjoiZDg2ZGVhMDUyMGQ5NGM3NWJjMTQ4MmIyOWE0NTBhN2IiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket Line 2", href="https://carrehomebusiness.atlassian.net/issues/?filter=10169&atlOrigin=eyJpIjoiMmUxNGMzNjM5NmNkNDRmY2E4NTExMmRiZTI2NTc0MWUiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket Line 4", href="https://carrehomebusiness.atlassian.net/issues/?filter=10170&atlOrigin=eyJpIjoiYjIxMjA0YTJjZGQ1NDlkMDk1NDRlYzc4MDE2ZGEyYjYiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket Line 7", href="https://carrehomebusiness.atlassian.net/issues/?filter=10171&atlOrigin=eyJpIjoiZDllY2FhYmFhZWFmNGY5MGFiYTUwMzcyMzg4ZjI0YzQiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket Linie 2", href="https://carrehomebusiness.atlassian.net/issues/?filter=10172&atlOrigin=eyJpIjoiMDYyMmQ5MDU4OWM0NGEzNTk4NjRkMzBmMjM3YWUxMWIiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket Linie 3", href="https://carrehomebusiness.atlassian.net/issues/?filter=10173&atlOrigin=eyJpIjoiNTJlOWNkMThjMzc1NDA1NmI0YTVmOTZhZTdlOTAyYjIiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket Linie 5", href="https://carrehomebusiness.atlassian.net/issues/?filter=10174&atlOrigin=eyJpIjoiY2JlMzk2YmQ0ODEwNDJmN2ExNjEwNjJkZDIwZGMzMjciLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket produit AMOX250C", href="https://carrehomebusiness.atlassian.net/issues/?filter=10175&atlOrigin=eyJpIjoiNDhiY2M2NDQ0OTgzNGYyNDg0MTFmODMyZGEzOTlkYTgiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket produit AMOX500", href="https://carrehomebusiness.atlassian.net/issues/?filter=10176&atlOrigin=eyJpIjoiNjllNDAxMTJmZTZkNGRkY2IxOGQ3OWY3ODIxYTJkMzYiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket produit ASPIRIN81", href="https://carrehomebusiness.atlassian.net/issues/?filter=10177&atlOrigin=eyJpIjoiM2JlZDk4ZTBlYmY3NDZlZGE2ZmNlZDBjY2YyMTRhYTMiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket produit IBUPRO200", href="https://carrehomebusiness.atlassian.net/issues/?filter=10178&atlOrigin=eyJpIjoiZGZkNGFmZWZjNmNiNDA0ZWI1MjkyZGIwMDAyYTc4ZTUiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket produit IBUPRO400", href="https://carrehomebusiness.atlassian.net/issues/?filter=10179&atlOrigin=eyJpIjoiMzhiMGI4NThiNTA5NGRiMjkxNzZhMGIxZGY2ZTlkMjEiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket produit PARA500MG", href="https://carrehomebusiness.atlassian.net/issues/?filter=10180&atlOrigin=eyJpIjoiMmJkODNlODRjOWRiNGQ1YmFhY2M2YmY1NWQ3MTE5ODgiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket produit VACCINX", href="https://carrehomebusiness.atlassian.net/issues/?filter=10181&atlOrigin=eyJpIjoiODc4MmUxNmFkMGJlNGZhNmJkYWJhNjlhOWYxMGU0YmYiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket produit VITD1000", href="https://carrehomebusiness.atlassian.net/issues/?filter=10182&atlOrigin=eyJpIjoiOGRlNjAwZDlmYjEyNGRhMjkyZmQyNThiZmU2M2JkYWMiLCJwIjoiaiJ9", target="_blank")),
                html.Li(html.A("Ticket produit ZINCPLUS", href="https://carrehomebusiness.atlassian.net/issues/?filter=10183&atlOrigin=eyJpIjoiZWJmZWE4ODllYTFjNGI5Yzk2M2ZhODcyOWRlYTk4MzIiLCJwIjoiaiJ9", target="_blank")),
            
            html.Div(style={"height": "20px"}), 
            html.H4("\U0001F4C4 Tableau par ticket"),
            html.Div(style={"height": "20px"}),
            html.Ul([ 
                html.Li(html.A("Tableau global des tickets", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10002", target="_blank")),
                html.Li(html.A("Tableau de Matthieu", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10036", target="_blank")),
                html.Li(html.A("Tableau de Lisa", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10034", target="_blank")),
                html.Li(html.A("Tableau de Stefan", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10035", target="_blank")),
                html.Li(html.A("Tableau de Jack", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10037", target="_blank")),
                html.Li(html.A("Tableau Ligne A1", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10067", target="_blank")),
                html.Li(html.A("Tableau Ligne B2", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10068", target="_blank")),
                html.Li(html.A("Tableau Ligne C4", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10069", target="_blank")),
                html.Li(html.A("Tableau Line 2", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10070", target="_blank")),
                html.Li(html.A("Tableau Line 4", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10071", target="_blank")),
                html.Li(html.A("Tableau Line 7", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10072", target="_blank")),
                html.Li(html.A("Tableau Linie 2", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10100", target="_blank")),
                html.Li(html.A("Tableau Linie 3", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10101", target="_blank")),
                html.Li(html.A("Tableau Linie 5", href="https://carrehomebusiness.atlassian.net/jira/dashboards/10102", target="_blank")),
            ]),
            ]),
        ], fluid=True)
        