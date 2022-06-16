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


