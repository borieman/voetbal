import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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


fig = px.histogram(FIFA15, x="overall", nbins = 10)
fig.update_traces(xbins=dict( # bins used for histogram
        start=40.0,
        end=95.0,
        size=5
    ))
st.plotly_chart(fig)




