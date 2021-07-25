import pandas as pd
import streamlit as st
df=pd.read_csv('States_RE.csv')

state=st.sidebar.selectbox('Select a state',df['StateName'].unique())
a=df[df['StateName']==state]
a['StateCode'].iloc[0]
