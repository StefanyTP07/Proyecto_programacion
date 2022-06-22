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
st.title("Análisis en Bonilla")
st.header("Tabla de datos:")
st.write(df_bonilla)
st.header("Histogramas de las concentraciones de contaminantes:")
df_bonilla['CO (ug/m3)'].plot.hist()
