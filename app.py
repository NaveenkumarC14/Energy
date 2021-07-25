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

<div class="col-md-3">
        <div class="card-style-3">
            <div class="card-body" style="height:150px;background-color: #d1f0a2">
                <div class="row">
                    <div class="col-xs-12 col-sm-12">
                        <div class="card-heading-1">'''+CO2+''' <span class="card-title-1">tCO<sub>2</sub></span> </div>
                        <div class="card-title-1">CO<sub>2</sub> emissions mitigated</div>                        
                        <div class="card-date-1">''' + CO2_Date +''' </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
''', unsafe_allow_html=True);
