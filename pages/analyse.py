from dash import dcc, register_page, html
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objects as go
from components import Box
from themes import theme_light as tl
import pandas as pd
import datetime
import plotly.express as px

pd.set_option('display.max_rows', 100)

today = datetime.date(2021, 11, 22)

'''
#Load Dataset and keep curre-nt date
trot = pd.read_csv('/home/adrien/development/python/charlotte_app/webapp_test/data/trotinettes.csv', sep=',', encoding='utf-8')

trot['date_scrapping'] = pd.to_datetime(trot['date_scrapping'], format="%d/%m/%Y %H:%M:%S")

trot = trot.loc[trot['date_scrapping'].dt.date == today]

nb_cumule = (len(trot)*91)
trot = trot.sort_values('date_scrapping').drop_duplicates(subset=['product_name', 'distributeur'], keep='last')

#Prepare prices
trot['prix'] = trot['prix'].replace(',', '.', regex=True)
trot['prix'] = trot['prix'].str.extract('(\d*\.\d+|\d+)')
trot['prix']= trot['prix'].replace('[\€,]', '', regex=True)
trot['prix']= trot['prix'].astype('float')

trot = trot[trot['prix'] > 50]
trot['distributeur'] = trot['distributeur'].replace('Aosom fr', 'aosom.fr', regex=True)



#Create min dataset

trot_min = trot.sort_values("prix").groupby("product_name", as_index=False).first()
trot_min['distributeur'] = trot_min['distributeur'].replace('Aosom fr', 'aosom.fr', regex=True)
trot_min = trot_min.add_suffix('_min')



#Merge trot and trot_min
trot = pd.merge(trot,trot_min[['product_name_min', 'prix_min', 'distributeur_min']],left_on='product_name', right_on='product_name_min', how='inner')


#calcul diff :
# Sort DataFrame before grouping.
trot = trot.sort_values(['product_name', 'distributeur', 'date_scrapping']).reset_index(drop=True)

# Group on keys and call `pct_change` inside `apply`.
trot['variation'] = (trot['prix'] - trot['prix_min']) / trot['prix_min'] * 100
trot['variation']= trot['variation'].astype('int')


#Frequency by shops 
freq_count=  trot.groupby(['distributeur','variation']).size().to_frame('count').reset_index()


def cat(x):
    if x > 0:
        return "Prix Supérieurs chez distributeur"
    if x < 0:
        return "Prix Inférieurs chez distributeur"
    elif x == 0:
        return "Prix Identiques chez distributeur"


freq_count['variation'] = freq_count['variation'].apply(lambda x: cat(x))

freq_count = freq_count.groupby(['distributeur', 'variation'])['count'].sum().to_frame('count').reset_index()

freq_total = freq_count.groupby(['distributeur'])['count'].sum().to_frame('total').reset_index()

freq = pd.merge(freq_count,freq_total,on='distributeur', how='inner')
freq['pourcentage'] = (freq['count'] / freq['total'] *100).round(1)

#Liste des cas interessants 

trot_diff = trot[trot['variation'] < 1]


trot_sample = trot_diff[trot_diff['distributeur'] != trot_diff['distributeur_min']]
trot_sample = trot_sample[['product_name', 'distributeur', 'prix', 'url', 'distributeur_min', 'prix_min',  'variation']]
trot_sample = trot_sample.sort_values(['variation'], ascending=False).reset_index(drop=True)

trot_sample['url'] = "https://www.idealo.fr" + trot_sample['url']

trot_sample.columns = ['Nom', 'Distributeur', 'Prix (€)', 'url', 'Distributeur_min','Prix minimum (€)', 'Variation (%)']

trot_drop_link = trot_sample.drop(columns=['url'])

nb_ref_uniq = 35

count_var = 20

freq = freq.sort_values(by=['pourcentage', 'variation'],ascending=False)  

print(trot_sample.shape[0])
    
#freq_chart = px.bar(freq, x="distributeur", y="pourcentage", color="variation", category_orders={"variation" : ["Prix Inférieurs chez distributeur", "Prix Identiques chez distributeur", "Prix Supérieurs chez distributeur"]}, color_discrete_map={'Prix Inférieurs chez distributeur': 'red','Prix Identiques chez distributeur': 'red', 'Prix Supérieurs chez distributeur': 'green'}, hover_data=["count", "total"])
#freq_chart.update_layout(legend_traceorder="reversed")'''

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


'''
children=dbc.Row(html.Div([html.Plaintext(children=f"Liste des {count_var} références avec prix identiques (variation < 1%)", style={"font-size": "20px", "font-family": "Open Sans", "color":"rgb(42,63,95)", "text-align": "center"}),
                                                          html.Plaintext(html.Table(
                                                                    # Header
                                                                    [html.Tr([html.Th(col, style={"outline": "thin solid", "line-height":"50px", "text-align": "center", "padding":"0 40px"}) for col in trot_drop_link.columns], style={"outline": "thin solid", "line-height":"50px", "text-align": "center", "padding":"0 40px"})] +

                                                                    # Body
                                                                    [html.Tr([
                                                                        html.Td(trot_sample.iloc[i][col], style={"outline": "thin solid", "text-align": "center"}) if col != 'Prix (€)' 
                                                                        else html.Td(html.A(id='my-id', href=f"{trot_sample.iloc[i]['url']}", title=trot_sample.iloc[i]['Nom'], children=trot_sample.iloc[i]['Prix (€)'], target='_blank'))
                                                                        for col in trot_drop_link.columns
                                                                    ], style={"outline": "thin solid", "text-align": "center"}) for i in range(len(trot_sample))]
                                                                                    )
                                                                        )
                                                        ])),style = {'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}
'''