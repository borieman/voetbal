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
# streamlit run your_script.py --server.maxUploadSize=1028


#st.set_page_config(layout="wide")

st.title('Fifa dashboard')

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





