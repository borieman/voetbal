import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.io as pio
pio.templates.default = 'seaborn'
import statsmodels.api as sm


st.beta_set_page_config(layout = "wide")

st.title('Fifa dashboard')

st.markdown("""
In dit dashboard hebben wij onderzocht ... . We hebben dit gedaan op basis van FIFA 15 t/m FIFA 22. 
Hiervoor hebben we https://www.kaggle.com/stefanoleone992/fifa-21-complete-player-dataset gebruikt voor de data.""")

st.write("""
***
""")




# countries = json.load(open('countries2.geojson', 'r'))

# kaartdata = pd.read_csv('kaartdata.csv')

# kaart = px.choropleth_mapbox(kaartdata, locations='id', geojson=countries, 
#                              color='overall', color_continuous_scale=[(0,"white"), (1,"green")],
#                              mapbox_style='open-street-map', center={'lat': 50, 'lon':0},
#                              zoom=0.62, opacity=0.6, hover_name='id', labels={'overall': '<b>Rating</b>'})
# #                              category_orders={'fifa_jaar': ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']},
# #                              animation_frame='fifa_jaar')
# kaart.update_layout(title='<b>KAARTGRAFIEK</b>', title_x=0.5, width=975, height=725)

# st.plotly_chart(kaart)

linedata = pd.read_csv('linedata.csv')



lijst_landen = ['Argentina', 'Belgium', 'Brazil', 'England', 'France', 'Germany', 'Italy', 'Netherlands', 'Portugal', 'Spain']
gekozen_landen = st.multiselect("Kies een land", lijst_landen, lijst_landen)

line_countries = linedata['nationality'].isin(gekozen_landen)
data = linedata[line_countries]

fig = px.line(data, x='fifa_jaar', y=['overall', 'potential'], color='nationality')


# dropdown_buttons = [{'label':"All", 'method':"update", 'args':
# [{"visible":[True]}]},
# {'label':"Argentina", 'method':"update", 'args':
# [{"visible":[True,True,False,False,False,False,False,False,False,False,False,False,
# False,False,False,False,False,False,False,False]}]},
# {'label':"Belgium", 'method':"update", 'args':
# [{"visible":[False,False,True,True,False,False,False,False,False,False,False,False,
# False,False,False,False,False,False,False,False]}]},
# {'label':"Brazil", 'method':"update", 'args':
# [{"visible":[False,False,False,False,True,True,False,False,False,False,False,False,
# False,False,False,False,False,False,False,False]}]},
# {'label':"England", 'method':"update", 'args':
# [{"visible":[False,False,False,False,False,False,True,True,False,False,False,False,
# False,False,False,False,False,False,False,False]}]},
# {'label':"France", 'method':"update", 'args':
# [{"visible":[False,False,False,False,False,False,False,False,True,True,False,False,
# False,False,False,False,False,False,False,False]}]},
# {'label':"Germany", 'method':"update", 'args':
# [{"visible":[False,False,False,False,False,False,False,False,False,False,True,True,
# False,False,False,False,False,False,False,False]}]},
# {'label':"Italy", 'method':"update", 'args':
# [{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,
# True,True,False,False,False,False,False,False]}]},
# {'label':"Netherlands", 'method':"update", 'args':
# [{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,
# False,False,True,True,False,False,False,False]}]},
# {'label':"Portugal", 'method':"update", 'args':
# [{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,
# False,False,False,False,True,True,False,False]}]},
# {'label':"Spain", 'method':"update", 'args':
# [{"visible":[False,False,False,False,False,False,False,False,False,False,False,False,
# False,False,False,False,False,False,True,True]}]}]

dropdown_buttons = [{'label':"All", 'method':"update", 'args':
[{"visible":[True]}]},
{'label':"Overall", 'method':"update", 'args':
[{"visible":[True, False]}]},
{'label':"Potential", 'method':"update", 'args':
[{"visible":[False, True]}]}]

fig.update_layout({'updatemenus':[{'type': "dropdown",'x': 1.23,'y': 0.30,
'showactive': True,'active': 0,'buttons': dropdown_buttons}]})

fig.update_layout(title='<b>Overall en potential rating per fifa per land</b>', title_x= 0.5,
xaxis_title='Fifa jaar', yaxis_title='Rating')


st.plotly_chart(fig)

#histogram

dfover = pd.read_csv('histover.csv')
dfpot = pd.read_csv('histpot.csv')

plot = go.Figure(data=[go.Histogram(
    name = 'Overall',
    x= dfover['value_eur']
),
    go.Histogram(
    name = 'Potential',
    x=dfpot['value_eur']
)
])

plot.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="Overall en Potential",
                     method="update",
                     args=[{"visible": [True, True]},
                           ]),
                dict(label="Overall",
                     method="update",
                     args=[{"visible": [True, False]},
                           ]),
                dict(label="Potential",
                     method="update",
                     args=[{"visible": [False, True]},
                           ]),
            ]),
         x= 1.43,y= 0.8)
    ])

plot.update_layout(title="<b>Waarde van spelers voor alle FIFA's</b>", title_x= 0.5,
                  xaxis_title='Waarde van speler',
                  yaxis_title='Aantal spelers')
  
st.plotly_chart(plot)

#fifa 15 lineair regressie

FIFA15_23 = pd.read_csv('FIFA15LIN.csv')
FIFA22_23 = pd.read_csv('FIFA22LIN.csv')

punt1 = pd.DataFrame({'overall': [93], 'value_eur': [54000000]})
punt2 = pd.DataFrame({'overall': [93], 'value_eur': [116000000]})

FIFA15_23['bestfit'] = sm.OLS(FIFA15_23['value_eur'],sm.add_constant(FIFA15_23['overall'])).fit().fittedvalues
FIFA22_23['bestfit'] = sm.OLS(FIFA22_23['value_eur'],sm.add_constant(FIFA22_23['overall'])).fit().fittedvalues


lin123 = go.Figure(data=[go.Scatter(
    name = 'FIFA15',
    x= FIFA15_23['overall'], y = FIFA15_23['value_eur'], mode='markers'
),
    go.Scatter(
    name = 'FIFA22',
    x=FIFA22_23['overall'], y = FIFA22_23['value_eur'], mode='markers'
),
    go.Scatter(name='Lineaire regressielijn FIFA15', x=FIFA15_23['overall'], y=FIFA15_23['bestfit'], mode='lines'
),  
    go.Scatter(name='Lineaire regressielijn FIFA22', x=FIFA22_23['overall'], y=FIFA22_23['bestfit'], mode='lines'
),
    go.Scatter(name='R2 & RSE FIFA15', x= punt1['overall'], y=punt1['value_eur'], mode='markers+text', text = "R2 = 0.728,RSE = 6450317",textposition = 'top left'
), 
    go.Scatter(name='R2 & RSE FIFA22', x= punt2['overall'], y=punt2['value_eur'], mode='markers+text', text = "R2 = 0.556,RSE = 19672194",textposition = 'bottom left')


])

lin123.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="FIFA15 & FIFA16",
                     method="update",
                     args=[{"visible": [True, True, True, True, True, True]},
                          ]),
                dict(label="FIFA15",
                     method="update",
                     args=[{"visible": [True, False, True, False, True, False]},
                           ]),
                dict(label="FIFA22",
                     method="update",
                     args=[{"visible": [False, True, False, True, False, True]},
                            ]),
                
            ]),
        x= 1.2,y= 0.8)
    ])
        
lin123.update_layout(title='<b>Waarde van spelers</b>', title_x= 0.5,
                  xaxis_title='Waarde van speler',
                  yaxis_title='Aantal spelers')

st.plotly_chart(lin123)

# FIFA15_23['bestfit'] = sm.OLS(FIFA15_23['value_eur'],sm.add_constant(FIFA15_23['overall'])).fit().fittedvalues
# fig15=go.Figure()
# fig15.add_trace(go.Scatter(name='',x=FIFA15_23['overall'], y=FIFA15_23['value_eur'].values, mode='markers'))
# fig15.add_trace(go.Scatter(name='Lineair regressielijn', x=FIFA15_23['overall'], y=FIFA15_23['bestfit'], mode='lines'))


# # plotly figure layout
# fig15.update_layout(title = '<b>Lineaire regressie van overall rating en de waarde van speler (FIFA15)<b>', xaxis_title = 'Overall rating', yaxis_title = 'Waarde speler in miljoenen')

# st.plotly_chart(fig15)


st.write("""
***
""")


st.markdown("""
Gemaakt door:
\n
Martijn Draper 
\n
Boris van Dam 500831201 """)

