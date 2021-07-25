import pandas as pd
import streamlit as st
df=pd.read_csv('States_RE.csv')

state=st.sidebar.selectbox('Select a state',df['StateName'].unique())
state=df[df['StateName']==state]
state_code=a['StateCode'].iloc[0]
str(state_code)

import requests as rq
url = "https://naveenkumarc_14.fred.sensetecnic.com/api/GetStateEnergy"
headers = { "Authorization" : "Basic bmF2ZWVua3VtYXJjXzE0Ok5hdmVlbkA2Ng==",
"Content-Type" : "application/json" }
post_body = {
	"StateCode" : 1
}
res = rq.post(url=url,data = post_body , headers = headers)

res.json()
