import streamlit as st
import pandas as pd
import numpy as np
import urllib.request
@st.experimental_memo
def download_data():
 url = 'https://drive.google.com/uc?id=17B8hm_07RhiLpL0GPhuvEQumycgzowez'
 filename = 'data.csv'
 urllib.request.urlretrieve(url, filename)
download_data()
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import scipy
df_bonilla = pd.read_csv('data.csv', sep=',', nrows=1000000, parse_dates=['Fecha', 'Longitud'])
#df_miraflores= pd.read_csv(r'https://www.datosabiertos.gob.pe/sites/default/files/Monitoreo_setiembre_Ov.Miraflores.xlsx', header= 0) 

st.title("Análisis Bonilla")
st.header("Tabla de datos")
st.write(df_bonilla)
for i in range(6,15):
    fig = px.histogram(df_bonilla, df_bonilla.columns[i])
    st.plotly_chart(fig, use_container_width=True)
