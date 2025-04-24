from dash import dcc, register_page, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from components import Box
from themes import theme_light as tl
import pandas as pd
import plotly.express as px

count_var = 20

# Directions Corporate
corporate_departments = [
    "Executive Directorate",
    "Directorate for Communications",
    "Directorate for Legal Affairs",
    "Council and Executive Committee Secretariat"
]
corporate_joiners = [5*3, 3*3, 2*3, 1*3]
corporate_resignations = [-4*3, -2*3, -1*3, -1*3]

# Directions Policy
policy_departments = [
    "Development Co-operation Directorate",
    "Directorate for Education and Skills",
    "Directorate for Employment, Labour and Social Affairs",
    "Directorate for Financial and Enterprise Affairs",
    "Directorate for Public Governance",
    "Directorate for Science, Technology and Innovation",
    "Economics Department",
    "Environment Directorate",
    "Global Relations and Co-operation Directorate",
    "Statistics and Data Directorate",
    "Trade and Agriculture Directorate",
    "OECD Development Centre"
]
policy_joiners = [6*3, 8*3, 7*3, 5*3, 6*3, 5*3, 4*3, 4*3, 3*3, 4*3, 5*3, 3*3]
policy_resignations = [-3*3, -6*3, -5*3, -4*3, -3*3, -4*3, -2*3, -3*3, -2*3, -3*3, -4*3, -2*3]

# Fusion
departments = corporate_departments + policy_departments
joiners = corporate_joiners + policy_joiners
resignations = corporate_resignations + policy_resignations

# Calcul des postes vacants
vacancies = [3,4,3,0,9,6,6,3,9,3,6,3,3,3,3,3]

freq_chart = go.Figure()

# Barres pour les recrutements
freq_chart.add_trace(go.Bar(
    x=departments,
    y=joiners,
    name='Recently joined staff',
    marker_color='green',
    text=joiners,
    textposition='inside'
))

# Barres pour les démissions
freq_chart.add_trace(go.Bar(
    x=departments,
    y=resignations,
    name='Recently departing staff',
    marker_color='red',
    text=[abs(r) for r in resignations],
    textposition='inside'
))

# Ajouter les boîtes de texte "postes vacants" au-dessus des barres
for i, dept in enumerate(departments):
    y_max = max(joiners[i], abs(resignations[i]))
    freq_chart.add_annotation(
        x=dept,
        y=y_max + 5,  # Position légèrement au-dessus du plus haut
        text=f"Vacancies: {vacancies[i]}",
        showarrow=False,
        font=dict(color="black", size=12),
        align="center",
        bgcolor="lightblue",
        bordercolor="gray",
        borderwidth=1,
        borderpad=4
    )

freq_chart.update_layout(
    title='Employees turnover by OECD Directorate (including available vacancies)',
    yaxis_title='Number of employees',
    barmode='relative',
    plot_bgcolor='white',
    xaxis_tickangle=-45,
    height=700
)

df = pd.read_csv('data/reviews.csv')
df = df.drop(df.filter(regex='Unnamed').columns, axis=1)

register_page(
    __name__,
    path='/')


COLORS = [
    str(tl.YELLOW),
    str(tl.ORANGE),
    str(tl.RED),
    str(tl.BLUE),
    str(tl.PURPLE)
]

#dbc.Row(html.Div([html.Plaintext(children="Insights from recent OECD Reviews on Glassdoor (scraped with Python/Selenium)", style={"font-size": "20px", "font-family": "Open Sans", "color":"rgb(42,63,95)", "text-align": "center"}),


layout = [
    dbc.Row([
        dbc.Col(
            Box(
                children=dbc.Row(
                    
                    html.Div([html.Plaintext(children="OECD Human Resource Management Service Health Indicators", style={"font-size": "20px", "font-family": "Open Sans", "color":"rgb(42,63,95)", "text-align": "center"}),
                    
                    dcc.Graph(
                    figure=go.Figure(go.Indicator(
                    domain = {'x': [0, 1], 'y': [0, 1]},
                    value = count_var,   #nombre de titre identiques aujourd'hui
                    mode = "gauge+number+delta",
                    #title = {'text': "Nombre de références avec prix identiques"},
                    delta = {'reference': 35}, #Nombre de prix identiques hier
                    gauge = {'axis': {'range': [None, 35]},
                            'steps' : [
                                {'range': [0, 17.5], 'color': "lightgray"},
                                {'range': [17.5, 31.5], 'color': "darkgray"},
                                {'range': [31.5, 35], 'color': "gray"}],
                            'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 35-count_var}},)
                    ))
            ]))
        )),
        dbc.Col([
            dbc.Row([
                dbc.Col(
                    Box(
                        children=dbc.Card(
                            [
                            dbc.CardHeader("Number of employees", style={'textAlign': 'center'}),
                            dbc.CardBody(
                                [
                                    html.H5(f"2356", className="card-title"),
                                ]
                                ,style={'textAlign': 'center'}),
                            ],
                        )
                    ),
                ),
            ],
            ),
            dbc.Row([
                dbc.Col(
                    Box(
                        children=dbc.Card(
                            [
                                dbc.CardHeader(f"Number of departing employees", style={'textAlign': 'center'}),
                                dbc.CardBody(
                                    [
                                        html.H5("212", className="card-title"),
                                    ]
                                    , style={'textAlign': 'center'}
                                ),
                            ],
                        )
                    ),
                ),
                dbc.Col(
                    Box(
                        children=dbc.Card(
                            [
                                dbc.CardHeader(f"Volontary exits not replaced", style={'textAlign': 'center'}),
                                dbc.CardBody(
                                    [
                                        html.H5("71", className="card-title"),
                                    ]
                                    , style={'textAlign': 'center'}
                                ),
                            ],
                        )

                    ),
                ),
            ]),
            dbc.Row([
                dbc.Col(
                    Box(
                        children=dbc.Card(
                            [
                                dbc.CardHeader(f"Turnover rate", style={'textAlign': 'center'}),
                                dbc.CardBody(
                                    [
                                        html.H5("9%", className="card-title"),
                                    ]
                                    , style={'textAlign': 'center'}
                                ),
                            ],
                        )
                    ),
                ),
                dbc.Col(
                    Box(
                        children=dbc.Card(
                            [
                                dbc.CardHeader(f"Attrition rate", style={'textAlign': 'center'}),
                                dbc.CardBody(
                                    [
                                        html.H5("3%", className="card-title"),
                                    ]
                                    , style={'textAlign': 'center'}
                                ),
                            ],
                        )

                    ),
                ),
            ]),
        ]),

        dbc.Row([
            dbc.Col(
                Box(
                    children=dcc.Graph(figure=freq_chart, config={"displaylogo": False, 'modeBarButtonsToRemove': ['zoom2d', 'hoverCompareCartesian', 'hoverClosestGeo', 'toggleSpikelines', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d']})
                ),
            )]),
        dbc.Row([
            dbc.Col(
                Box(
                    children=dbc.Row(children=dbc.Row(html.Div([html.Plaintext(children="Insights from recent OECD Reviews on Glassdoor (scraped with Python/Selenium)", style={"font-size": "20px", "font-family": "Open Sans", "color":"rgb(42,63,95)", "text-align": "center"}),
                                                          dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)
                                                        ])),style = {'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),style = {'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}
                ),
            )])
    ])]
