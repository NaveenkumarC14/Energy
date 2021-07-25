import pandas as pd
import streamlit as st
df=pd.read_csv('States_RE.csv')

state=st.sidebar.selectbox('Select a state',df['StateName'].unique())
state=df[df['StateName']==state]
state_code=a['StateCode'].iloc[0]
str(state_code)


url = 
