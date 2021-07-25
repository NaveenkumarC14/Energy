import pandas as pd
import streamlit as st
df=pd.read_csv('States_RE.csv')

state=st.selectbox('Select a state',df['State'].unique())
state=df[df['State']==state]
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
stateName = str(res.json()["StateName"]) + ""
CO2 = str(res.json()["CO2"]) + " tCO2"
CO2_Date  = str(res.json()["CO2_Date"]) + ""
solar_gen = str(res.json()["solar_gen"]) + "MU"
solar_gen_date = str(res.json()["solar_gen_date"]) + ""
wind_gen = str(res.json()["wind_gen"]) + "MU"
re_capacity = str(res.json()["re_capacity"]) + "MW"
re_capacity_date = str(res.json()["re_capacity_date"]) + ""


st.markdown('''

<h1></h1>
<div class="jumbotron text-center" style='padding: 0px';background-color:#fff>
 <div class="row" style="background-color:#fff;width:100%;margin:auto;">
<div 
      <div class="row-sm-4">
      <p style='text-align:center;  font-size: 15px; color: green'>Solar</p>
      <p style='text-align: center; font-size: 15px; color: green'></p>
     <p style='text-align: center ; font-size: 42px; font-weight: bold; color: blue'>''' + str(CO2) +'''</p>
     </div>
      </div>
 <div 
     <div class="row-sm-4">
      <p style='text-align:center;  font-size: 15px; color: green'>Solar</p>
      <p style='text-align: center; font-size: 15px; color: green'></p>
     <p style='text-align: center ; font-size: 42px; font-weight: bold; color: green'>''' + str(solar_gen) +'''</p>
      </div>
      </div>
   <div 
      <p style='text-align:center;  font-size: 15px; color: green'>RE Capasity</p>
      <p style='text-align: center; font-size: 15px; color: green'></p>
     <p style='text-align: center ; font-size: 42px; font-weight: bold; color: red'>''' + str(re_capacity) +'''</p>
     </div>
 

</div>

 ''', unsafe_allow_html=True);
