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
X = sm.add_constant(FIFA15["overall"])
y = FIFA15["value_eur"]

# Note the difference in argument order
model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

# Print out the statistics
model.summary()



