# app.py, run with 'streamlit run app.py'

#import pip
#pip.main(["install", "openpyxl"])
#pip.main(["install", "pandas"])
#import plotly.figure_factory as ff
#pip.main(["install", "matplotlib"])
#1tReqZLXKH569JkzNQ7cc8kTFA11UdN6qI2PgvDvE6zs
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import scipy
import gdown

@st.experimental_memo
def download_data():
  url = 'https://docs.google.com/uc?id=1tReqZLXKH569JkzNQ7cc8kTFA11UdN6qI2PgvDvE6zs'
  output = 'data.csv'
  gdown.download(url,output, quiet= False)
  return filename


st.write(download_data())

