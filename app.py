import pandas as pd
import streamlit as st
import plotly.express as px
df=pd.read_csv('States_RE.csv')

daily_gen=pd.read_csv("India's DailyGeneration (15 June, 2005 to 24 July, 2021).csv")
install_capa=pd.read_csv("India's InstalledCapacity.csv")
month_gen=pd.read_csv("India's MonthlyGeneration.csv")
		
st.markdown('''
<div class="jumbotron text-center" style='background-color: #fff'>
  <h1 style="margin: auto; width: 100%;">Renewables India Dashboard</h1>
  <h2></h2><p style="margin: auto; font-weight: bold; text-align: center; width: 100%;">Renewable Energy Live Update in India</p>
  <h3></h3>
 
</div>
''', unsafe_allow_html=True);
					     
state1=st.selectbox('Select a state',df['State'].unique())
state=df[df['State']==state1]
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
CO2 = str(res.json()["CO2"]) + ""
CO2_Date  = str(res.json()["CO2_Date"]) + ""
solar_gen = str(res.json()["solar_gen"]) + "MU"
solar_gen_date = str(res.json()["solar_gen_date"]) + ""
wind_gen = str(res.json()["wind_gen"]) + "MU"
re_capacity = str(res.json()["re_capacity"]) + "MW"
re_capacity_date = str(res.json()["re_capacity_date"]) + ""


st.markdown('''
	<div class="jumbotron text-center" style='background-color: #fff'>
	   <h1></h1>
	   <p style="margin: auto; font-weight: 400; text-align: center; width: 100%;">Last Updated: ''' + str(CO2_Date) + '''</p>
	   <h2></h2>
	</div>
	''', unsafe_allow_html=True);



st.markdown('''

	<div class="col-md-3">
		<div class="card-style-3">
		    <div class="card-body" style="height:150px;background-color: #d1f0a2">
			<div class="row">
			    <div class="col-xs-12 col-sm-12">
	<div
				<p style='text-align: center; font-size: 40px; font-weight: 600; color:  blue'>''' + str(CO2) +  ''' <span class="card-title-1">tCO<sub>2</sub></span></p></div>
				<div 
				<p style ='text-align: center; background-color: #d1f0a2; font-weight: 400 ;color:  blue'>CO2 emissions mitigated</p> </div>  
				<div 
				<p style ='text-align: center; background-color: #d1f0a2; font-weight: 400 ;color:  blue'>''' + str(CO2_Date) + '''</p></div> 
			    <div 
				<p style ='text-align: center; background-color: #d1f0a2; font-weight: 400 ;color: blue'></p>
				</div>  
			    </div>
			</div>
		    </div>
		</div>
	    </div>
	''', unsafe_allow_html=True);

st.markdown('''

	<div class="col-md-3">
		<div class="card-style-3">
		    <div class="card-body" style="height:150px;background-color: white">
			<div class="row">
			    <div class="col-xs-12 col-sm-12">
	<div
				<p style='text-align: center; font-size: 40px; font-weight: 600; color:  blue'>''' + str(solar_gen) +  '''</p></div>
				<div 
				<p style ='text-align: center; background-color: white; font-weight: 400 ;color:  blue'>Solar Generation</p> </div>  
				<div 
				<p style ='text-align: center; background-color: white; font-weight: 400 ;color:  blue'>''' + str(solar_gen_date) + '''</p></div> 
			    <div 
				<p style ='text-align: center; background-color: white; font-weight: 400 ;color: blue'></p>
				</div>  
			    </div>
			</div>
		    </div>
		</div>
	    </div>
	''', unsafe_allow_html=True);

st.markdown('''

	<div class="col-md-3">
		<div class="card-style-3">
		    <div class="card-body" style="height:150px;background-color: #d1f0a2">
			<div class="row">
			    <div class="col-xs-12 col-sm-12">
	<div
				<p style='text-align: center; font-size: 40px; font-weight: 600; color:  blue'>''' + str(wind_gen) +  '''</p></div>
				<div 
				<p style ='text-align: center; background-color: #d1f0a2; font-weight: 400 ;color:  blue'>Wind Generation</p> </div>  
				<div 
				<p style ='text-align: center; background-color: #d1f0a2; font-weight: 400 ;color:  blue'>''' + str(solar_gen_date) + '''</p></div> 
			    <div 
				<p style ='text-align: center; background-color: white; font-weight: 400 ;color: blue'></p>
				</div>  
			    </div>
			</div>
		    </div>
		</div>
	    </div>
	''', unsafe_allow_html=True);

st.markdown('''

	<div class="col-md-3">
		<div class="card-style-3">
		    <div class="card-body" style="height:150px;background-color:white">
			<div class="row">
			    <div class="col-xs-12 col-sm-12">
	<div
				<p style='text-align: center; font-size: 40px; font-weight: 600; color:  blue'>''' + str(re_capacity) +  '''</p></div>
				<div 
				<p style ='text-align: center; background-color: white; font-weight: 400 ;color:  blue'>Installed RE Capacity</p> </div>  
				<div 
				<p style ='text-align: center; background-color: white; font-weight: 400 ;color:  blue'>''' + str(re_capacity_date) + '''</p></div> 
			    <div 
				<p style ='text-align: center; background-color: white; font-weight: 400 ;color: blue'></p>
				</div>  
			    </div>
			</div>
		    </div>
		</div>
	    </div>
	''', unsafe_allow_html=True);


if state1=='All':
	
	st.markdown('''
		<div class="jumbotron text-center" style='background-color: #fff'>
		  <h1 style="margin: auto; width: 100%;">RE Generation (Tentative)</h1>
		</div>
		 ''', unsafe_allow_html=True);
	daily_gen2=pd.melt(daily_gen,id_vars = 'Date', var_name="Source", value_name="Value")	

	fig = px.line(daily_gen2, x="Date", y="Value", color="Source",line_group="Source", hover_name="Date", width=1000, height=500)
	st.plotly_chart(fig)

	st.markdown('''
		<div class="jumbotron text-center" style='background-color: #fff'>
		  <h1 style="margin: auto; width: 100%;">RE Generation</h1>
		</div>
		 ''', unsafe_allow_html=True);
	daily_gen3=pd.melt(month_gen,id_vars = 'Month', var_name="Source", value_name="Value")	

	fig = px.line(daily_gen3, x="Month", y="Value", color="Source",line_group="Source", hover_name="Month", width=1000, height=500)
	st.plotly_chart(fig)

	st.markdown('''
		<div class="jumbotron text-center" style='background-color: #fff'>
		  <h1 style="margin: auto; width: 100%;">Install Capacity</h1>
		</div>
		 ''', unsafe_allow_html=True);
	install_capa1=pd.melt(install_capa,id_vars = 'Month', var_name="Source", value_name="Value")	
        
	fig =px.bar(install_capa1,x='Month',y="Value",color='Source',barmode='group', width=1000, height=500)
	st.plotly_chart(fig)
       
	ut=pd.read_csv("India's Capacity Utilisation.csv")
	st.markdown('''
		<div class="jumbotron text-center" style='background-color: #fff'>
		  <h1 style="margin: auto; width: 100%;">Capacity Utilisation</h1>
		</div>
		 ''', unsafe_allow_html=True);
	install_capa1=pd.melt(ut,id_vars = 'Month', var_name="Source", value_name="Value")	
        
	fig = px.pie(install_capa1,values='Value',names='Source')
	st.plotly_chart(fig)
	fig=px.bar(install_capa1,x='Month',y="Value",color='Source',barmode='group', width=1000, height=500)
	st.plotly_chart(fig)
