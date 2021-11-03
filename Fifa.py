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



#st.set_page_config(layout="wide")

st.title('Fifa dashboard')

st.write("""
***
""")

FIFA15 = pd.read_csv('FIFA15')


fig = px.histogram(FIFA15, x="overall", nbins = 10, title = "Aantal spelers per rating")
fig.update_traces(xbins=dict( # bins used for histogram
        start=40.0,
        end=95.0,
        size=5
    ))
st.plotly_chart(fig)

countries = json.load(open('countries2.geojson', 'r'))

kaartdata = pd.read_csv('kaartdata.csv')

kaart = px.choropleth_mapbox(kaartdata, locations='id', geojson=countries, 
                             color='overall', color_continuous_scale=[(0,"white"), (1,"green")],
                             mapbox_style='open-street-map', center={'lat': 50, 'lon':0},
                             zoom=0.62, opacity=0.6, hover_name='id', labels={'overall': '<b>Rating</b>'},
                             category_orders={'fifa_jaar': ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']},
                             animation_frame='fifa_jaar')
kaart.update_layout(title='<b>KAARTGRAFIEK</b>', title_x=0.5, width=975, height=725)

st.plotly_chart(kaart)



