import pandas as pd
import streamlit as st
df=pd.read_csv('States_RE.csv')

state=st.sidebar.selectbox('Select a state',df['StateName'].unique())
state=df[df['StateName']==state]
state_code=state['StateCode'].iloc[0]
#str(state_code)

import requests as rq
#import ujson as json
url = "https://naveenkumarc_14.fred.sensetecnic.com/api/GetStateEnergy?st=" +str(state_code)
#r=rq.get("https://naveenkumarc_14.fred.sensetecnic.com/api/GetStateEnergy?st=1",auth = ("naveenkumarc_14", "Naveen@66"))
#r.status_code
headers = { 
		"Content-Type" : "application/json",
	  	"Accept" : "application/json" 
	   }
post_body = {
	"StateCode" : 1
}
res = rq.get(url, auth = ("naveenkumarc_14", "Naveen@66"))
res.text
#json.literal_eval(res.text)

jsonData = st.json(res.text)

(res.json()["StateName"])
