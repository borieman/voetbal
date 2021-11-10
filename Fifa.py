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


st.write("""
***
""")

page_names = ['Hoofdmenu', 'Lijngrafiek', 'Boxplot', 'Kaartgrafiek', 'Polar chart', 'Histogram', 'Lineaire Regressie']
page = st.sidebar.radio('Menu', page_names, index=1)

if page == 'Hoofdmenu':
    st.markdown("""
In dit dashboard hebben wij onderzocht uit welke landen de beste voetbalspelers hebben en welke aspecten/eigenschappen bijdragen aan een goede (potentiële) voetballler.
Met behulp van figuren hebben wij dit inzichtelijk gemaakt. In het verloop van het onderzoek hebben wij ons gefocust op de 23 beste spelers van de beste 10 landen. 
Voor het onderzoek hebben wij gebruik gemaakt van de datasets van FIFA 15 t/m FIFA 22 en hierbij hebben we gekeken naar zowel overall rating als potential rating. 
Uit het onderzoek is naar voren gekomen dat de volgende aspecten/eigenschappen voorkomen bij goede voetballers (in fifa):
\n
•Afkostmig uit Argentinië, België, Brazilië, Engeland, Frankrijk, Duitsland, Italië, Nederland, Portugal of Spanje.
\n
•Een leeftijd rond de 30. De overall rating van oudere spelers is hoger dan die van jongere spelers (wel hebben jongere spelers een hoge potential rating).
\n
•Een hoge waarde. Er is een verband tussen overall rating en waarde van een speler. 
\n
\n
\n
Bron: https://www.kaggle.com/stefanoleone992/fifa-21-complete-player-dataset """) 
    
#Lijngrafiek    
if page == 'Lijngrafiek':
  linedata = pd.read_csv('linedata.csv')

  lijst_landen = ['Argentina', 'Belgium', 'Brazil', 'England', 'France', 'Germany', 'Italy', 'Netherlands', 'Portugal', 'Spain']
  gekozen_landen = st.multiselect("Kies een land", lijst_landen, lijst_landen)

  line_countries = linedata['nationality'].isin(gekozen_landen)
  data = linedata[line_countries]

  fig = px.line(data, x='fifa_jaar', y=['overall', 'potential'], color='nationality')

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
              
#boxplot
if page == 'Boxplot':
  boxdata = pd.read_csv('boxdata.csv')

  box = px.box(boxdata, x='age', y='nationality', color='soort')
  box.update_layout(title='<b>Spreiding leeftijd Fifa 2022 voor overall en potential</b>', title_x= 0.5,
                      xaxis_title='Leeftijd', yaxis_title='Landen', height=825, width=1475)
  st.plotly_chart(box)            

#Kaart
if page == 'Kaartgrafiek':
    st.write('De kaart kan helaas niet online worden weergegeven via hier.')   
              
#polar chart
if page == 'Polar chart':
    PC22_23 = pd.read_csv('PolarChartOverall.csv')
    PC22_23P = pd.read_csv('PolarChartPotential.csv')
    
    theta = ['Pace', 'Shooting', 'Passing', 'Dribbling', 'Defending', 'Physic', 'Pace']

    # Adding stats to every country
    Argentina_stats = [76, 76, 77, 82, 57, 74, 76]
    Belgium_stats = [74, 71, 76, 78, 59, 72, 74]
    Brazil_stats = [74, 68, 75, 78, 70, 77, 74]
    England_stats = [76, 67, 77, 79, 66, 74, 76]
    France_stats = [81, 69, 75, 80, 63, 76, 81]
    Germany_stats = [71, 74, 78, 78, 65, 75, 71]
    Italy_stats = [74, 65, 72, 77, 68, 73, 74]
    Netherlands_stats = [73, 69, 73, 76, 66, 78, 73]
    Portugal_stats = [73, 72, 77, 80, 64, 73, 73]
    Spain_stats = [72, 71, 80, 81, 69, 71,  72]

    # Adding stats to every country
    Argentina_statsP = [78, 68, 72, 78, 55, 68, 78]
    Belgium_statsP = [75, 65, 70, 75, 53, 67, 75]
    Brazil_statsP = [81, 67, 71, 79, 56, 71, 81]
    England_statsP = [79, 67, 73, 79, 56, 67, 79]
    France_statsP = [80, 61, 72, 78, 66, 74, 80]
    Germany_statsP = [73, 67, 74, 76, 61, 70, 73]
    Italy_statsP = [73, 64, 70, 76, 64, 72, 73]
    Netherlands_statsP = [78, 63, 68, 74, 58, 74, 78]
    Portugal_statsP = [78, 70, 72, 79, 55, 70, 78]
    Spain_statsP = [73, 70, 77, 79, 64, 69, 73]
    

    fig = make_subplots(rows=1, cols=3, 
                    specs=[[{'type': 'xy'}, {"type": "polar"}, {'type': 'xy'},]],
                    column_widths=[0.3, 0.7, 0.3])

    fig.add_trace(go.Scatterpolar(r=Argentina_stats, theta=theta, fill='toself',
             hovertemplate='<b>%{theta}</b>' + f'<b>: '+'%{r}', showlegend=False, name='Argentina',
             line=dict(color='Aqua')), row=1, col=2)

    fig.add_trace(go.Scatterpolar(r=Belgium_stats, theta=theta, fill='toself',
             hovertemplate='<b>%{theta}</b>' + f'<b>: '+'%{r}', showlegend=False, name='Belgium',
             line=dict(color='Crimson')), row=1, col=2)

    fig.add_trace(go.Scatterpolar(r=Brazil_stats, theta=theta, fill='toself',
             hovertemplate='<b>%{theta}</b>' + f'<b>: '+'%{r}', showlegend=False, name='Brazil',
             line=dict(color='Yellow')), row=1, col=2)

    fig.add_trace(go.Scatterpolar(r=England_stats, theta=theta, fill='toself',
             hovertemplate='<b>%{theta}</b>' + f'<b>: '+'%{r}', showlegend=False, name='England',
             line=dict(color='White')), row=1, col=2)

    fig.add_trace(go.Scatterpolar(r=France_stats, theta=theta, fill='toself',
             hovertemplate='<b>%{theta}</b>' + f'<b>: '+'%{r}', showlegend=False, name='France',
             line=dict(color='Black')), row=1, col=2)

    fig.add_trace(go.Scatterpolar(r=Germany_stats, theta=theta, fill='toself',
             hovertemplate='<b>%{theta}</b>' + f'<b>: '+'%{r}', showlegend=False, name='Germany',
             line=dict(color='Gray')), row=1, col=2)

    fig.add_trace(go.Scatterpolar(r=Italy_stats, theta=theta, fill='toself',
             hovertemplate='<b>%{theta}</b>' + f'<b>: '+'%{r}', showlegend=False, name='Italy',
             line=dict(color='Navy')), row=1, col=2)

    fig.add_trace(go.Scatterpolar(r=Netherlands_stats, theta=theta, fill='toself',
             hovertemplate='<b>%{theta}</b>' + f'<b>: '+'%{r}', showlegend=False, name='Netherlands',
             line=dict(color='Orange')), row=1, col=2)

    fig.add_trace(go.Scatterpolar(r=Portugal_stats, theta=theta, fill='toself',
             hovertemplate='<b>%{theta}</b>' + f'<b>: '+'%{r}', showlegend=False, name='Portugal',
             line=dict(color='Darkgreen')), row=1, col=2)

    fig.add_trace(go.Scatterpolar(r=Spain_stats, theta=theta, fill='toself',
             hovertemplate='<b>%{theta}</b>' + f'<b>: '+'%{r}', showlegend=False, name='Spain',
             line=dict(color='Red')), row=1, col=2)

    fig.add_trace(go.Scatterpolar(r=Argentina_statsP, theta=theta, fill='toself',
             hovertemplate='<b>%{theta}</b>' + f'<b>: '+'%{r}', showlegend=False, name='Argentina',
             line=dict(color='Aqua')), row=1, col=2)

    fig.add_trace(go.Scatterpolar(r=[Belgium_statsP, Brazil_statsP], theta=theta, fill='toself',
             hovertemplate='<b>%{theta}</b>' + f'<b>: '+'%{r}', showlegend=False, name='Belgium',
             line=dict(color='Crimson')), row=1, col=2)

    fig.add_trace(go.Scatterpolar(r=Brazil_statsP, theta=theta, fill='toself',
             hovertemplate='<b>%{theta}</b>' + f'<b>: '+'%{r}', showlegend=False, name='Brazil',
             line=dict(color='Yellow')), row=1, col=2)

    fig.add_trace(go.Scatterpolar(r=England_statsP, theta=theta, fill='toself',
             hovertemplate='<b>%{theta}</b>' + f'<b>: '+'%{r}', showlegend=False, name='England',
             line=dict(color='White')), row=1, col=2)

    fig.add_trace(go.Scatterpolar(r=France_statsP, theta=theta, fill='toself',
             hovertemplate='<b>%{theta}</b>' + f'<b>: '+'%{r}', showlegend=False, name='France',
             line=dict(color='Black')), row=1, col=2)

    fig.add_trace(go.Scatterpolar(r=Germany_statsP, theta=theta, fill='toself',
             hovertemplate='<b>%{theta}</b>' + f'<b>: '+'%{r}', showlegend=False, name='Germany',
             line=dict(color='Gray')), row=1, col=2)

    fig.add_trace(go.Scatterpolar(r=Italy_statsP, theta=theta, fill='toself',
             hovertemplate='<b>%{theta}</b>' + f'<b>: '+'%{r}', showlegend=False, name='Italy',
             line=dict(color='Navy')), row=1, col=2)

    fig.add_trace(go.Scatterpolar(r=Netherlands_statsP, theta=theta, fill='toself',
             hovertemplate='<b>%{theta}</b>' + f'<b>: '+'%{r}', showlegend=False, name='Netherlands',
             line=dict(color='Orange')), row=1, col=2)

    fig.add_trace(go.Scatterpolar(r=Portugal_statsP, theta=theta, fill='toself',
             hovertemplate='<b>%{theta}</b>' + f'<b>: '+'%{r}', showlegend=False, name='Portugal',
             line=dict(color='Darkgreen')), row=1, col=2)

    fig.add_trace(go.Scatterpolar(r=Spain_statsP, theta=theta, fill='toself',
             hovertemplate='<b>%{theta}</b>' + f'<b>: '+'%{r}', showlegend=False, name='Spain',
             line=dict(color='Red')), row=1, col=2)

    fig.update_layout(
        title=f'<b>Gemiddelde stats per land</b>',
         paper_bgcolor = "rgb(223, 223, 223)",
        polar=dict(
            bgcolor = "rgb(223, 223, 223)",
             radialaxis=dict(
                        visible = True,
                        range = [50, 85]
                            )
                   ), 
        template='xgridoff',
        font=dict(
                  family='Arials',
                  size=16, 
                  color='Black'
                 )
    )

    Polardropdown = [{'label':"All", 'method':"update", 'args':[{"visible":[
        True, True, True, True, True, True, True, True, True, True, 
        True, True, True, True, True, True, True, True, True, True]}]},
                     {'label':"None", 'method':"update", 'args':[{"visible":[
        False, False, False, False, False, False, False, False, False, False, 
        False, False, False, False, False, False, False, False, False, False]}]},
                 {'label':"Overall", 'method':"update", 'args':[{"visible":[
        True, True, True, True, True, True, True, True, True, True, 
        False, False, False, False, False, False, False, False, False, False]}]},
                 {'label':"Potential", 'method':"update", 'args':[{"visible":[
        False, False, False, False, False, False, False, False, False, False, 
        True, True, True, True, True, True, True, True, True, True]}]}]

    fig.update_layout({'updatemenus':[{'type': "dropdown",'x': 0,'y': 1.4,
                                       'showactive': True,'active': 0,'buttons': Polardropdown}]})

    st.plotly_chart(fig)
             
              
#histogram
if page == 'Histogram':
  dfover = pd.read_csv('histover.csv')
  dfpot = pd.read_csv('histpot.csv')

  plot = go.Figure(data=[go.Histogram(
        name = 'Overall Rating',
        x= dfover['value_eur']
    ),
        go.Histogram(
        name = 'Potential Rating',
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
          x= 1.26,y= 0.8)
       ])

  plot.update_layout(title="<b>Waarde van spelers voor alle FIFA's</b>", title_x= 0.5,
                  xaxis_title='Waarde van speler',
                  yaxis_title='Aantal spelers')
  
  st.plotly_chart(plot)    
    


#lineair regressie
if page == 'Lineaire Regressie':
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
                    dict(label="FIFA15 & FIFA22",
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
         x= 1.23,y= 0.52)
       ])
        
    lin123.update_layout(title='<b>Lineaire regressie overall rating en waarde speler FIFA15 & FIFA22</b>', title_x= 0.5,
                  xaxis_title='Overall rating',
                  yaxis_title='Waarde speler', width = 1000)

    st.plotly_chart(lin123)




st.write(""" ***""")




st.markdown("""
Gemaakt door:
\n
Martijn Draper 500888847
\n
Boris van Dam 500831201 """)

