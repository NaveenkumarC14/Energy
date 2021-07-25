import pandas as pd
import streamlit as st
df=pd.read_csv('States_RE.csv')

state=st.sidebar.selectbox('Select a state',df['StateName'].unique())
state=df[df['StateName']==state]
state_code=state['StateCode'].iloc[0]
#str(state_code)

import requests as rq
url = "https://naveenkumarc_14.fred.sensetecnic.com/api/GetStateEnergy?st=1"
r=rq.get("https://naveenkumarc_14.fred.sensetecnic.com/api/GetStateEnergy?st=1",auth = ("naveenkumarc_14", "Naveen@66")
r.status_code
headers = { 
		"Content-Type" : "application/json",
	  	"Accept" : "application/json" 
	   }
post_body = {
	"StateCode" : 1
}
res = rq.get(url,data = post_body , headers = headers, auth = ("naveenkumarc_14", "Naveen@66"))
res

url
headers
post_body
#print(res.text)
