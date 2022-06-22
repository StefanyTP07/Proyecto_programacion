#app.py, run with 'streamlit run app.py'

import pip
pip.main(["install", "openpyxl"])
pip.main(["install", "pandas"])
import plotly.figure_factory as ff
pip.main(["install", "matplotlib"])
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import scipy

df_bonilla = pd.read_excel(r'https://www.datosabiertos.gob.pe/sites/default/files/Monitoreo_setiembre_Bonilla.xlsx', header= 0) 
df_miraflores= pd.read_excel(r'https://www.datosabiertos.gob.pe/sites/default/files/Monitoreo_setiembre_Ov.Miraflores.xlsx', header= 0) 
st.title("Monitoreo de calidad de aire QAIRA - [Municipalidad de Miraflores]")
st.header("Integrantes:")
st.write("-Stefany Tumpay Paredes")
st.write("-Jener Cesar Huincho Ramos")
st.write("-Gianina Berduzco Ancco")
st.write("-Teyzon Florida Serrepe")
st.write("-Alvaro Ivan Alarcon Guizado")
st.header("Contexto")
st.write("“Saber la calidad de aire que se respira en un determinado lugar es importante para los ciudadanos que habitan en ella”. Por ello, en esta página se presenta un análisis estadístico de contaminantes presente en la Municipalidad de Miraflores-Lima(Perú). La base de datos fue proporcionada por la municipalidad mencionada, de esta manera se escogió los datos de monitoreo del Complejo Deportivo Bonilla y Ovalo Miraflores, los datos de estos dos lugares de monitoreo corresponden al mes de septiembre del 2020. Esta presentación incluye cuatro partes: Gráfica de datos de los respectivos contaminantes en Bonilla y Ov.Miraflores, gráficas comparativas entre ambos lugares y por último comparaciones de sus Límites Máximos Permisibles.")

st.title("Análisis en Bonilla")
st.header("Tabla de datos:")
st.write(df_bonilla)
co=df_bonilla['CO (ug/m3)']
st.hist_chart(co)
