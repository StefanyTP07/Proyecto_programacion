# app.py, run with 'streamlit run app.py'

import pip
#pip.main(["install", "openpyxl"])
#pip.main(["install", "pandas"])
#import plotly.figure_factory as ff
#pip.main(["install", "matplotlib"])
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

df_bonilla = pd.read_excel(r'https://www.datosabiertos.gob.pe/sites/default/files/Monitoreo_setiembre_Bonilla.xlsx', header= 0) 
df_miraflores= pd.read_excel(r'https://www.datosabiertos.gob.pe/sites/default/files/Monitoreo_setiembre_Ov.Miraflores.xlsx', header= 0) 
# df = pd.read_excel(...)  # will work for Excel files

st.title("Tabla Bonilla")  # add a title
st.write(df_miraflores.dtypes.astype(str))
#df_bonilla.iloc[:, 6:14].hist()
#st.line_chart(pd.concat([df_bonilla.iloc[:, 6],df_miraflores.iloc[:, 6]], axis = 1))
st.write(df_bonilla.iloc[:, 6])
st.write(df_miraflores.iloc[:, 6])
st.write(df_bonilla.columns[6])
st.write(df_miraflores.columns[6])
st.write(pd.merge(df_bonilla.iloc[:, 6], df_miraflores.iloc[:, 6], on=df_bonilla.columns[6]))
st.line_chart(pd.merge(df_bonilla.iloc[:, 6], df_miraflores.iloc[:, 6], on=df_bonilla.columns[6]))
#plt.show()
#st.pyplot()
#st.write()  # visualize my dataframe in the Streamlit app
st.title("Tabla Miraflores")  # add a title
st.write(df_miraflores)  # visualize my dataframe in the Streamlit app
