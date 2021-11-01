import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import json
# import requests
# !pip install geopandas
# import streamlit as st
# from streamlit_folium import folium_static
# import folium
# import folium
# import plotly.express as px
# import plotly.graph_objects as go
# import plotly.figure_factory as ff
# import plotly.io as pio
# pio.templates.default = 'seaborn'
# import statsmodels.api as sm



#st.set_page_config(layout="wide")

st.title('Fifa dashboard')

st.write("""
***
""")


FIFA22_map = pd.read_csv('mapdata')

geo = gpd.read_file('countries2.geojson')
countries = geo.rename(columns={'ADMIN': 'nationality'})

df = gpd.GeoDataFrame(pd.merge(FIFA22_map, countries, how = 'left', on = 'nationality'))

# m = folium.Map(location=[0, 0],
#                zoom_start=2)

# folium.Choropleth(geo_data=df,
#                   name='geometry',
#                   data=df,
#                   columns=['nationality','overall'],
#                   key_on='feature.properties.nationality', 
#                   fill_color='YlGn', 
#                   fill_opacity=0.9, 
#                   line_opacity=0.3,
#                   legend_name='Lagenda: Rating', 
#                   nan_fill_color='black').add_to(m)

# display(m)
