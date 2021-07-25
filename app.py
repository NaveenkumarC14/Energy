import pandas as pd
import streamlit as st
df=pd.read_csv('States_RE.csv')
st.sidebar.selectbox('Select a state',df['StateName'].unique())
