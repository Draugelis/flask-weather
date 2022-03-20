from flask import Flask, render_template, request
import requests

app 	= Flask(__name__)

@app.route('/')
def home():
	ip	= request.remote_addr
	if ip == "127.0.0.1":
		location = "Vilnius"
	else:
		location_request 	= requests.get(f"http://ip-api.com/json/{ip}")
		location_data		= location_request.json()
		location 			= location_data['city']

	weather_request = requests.get(f"https://weatherdbi.herokuapp.com/data/weather/{location}")
	weather_data 	= weather_request.json()
	temp  			= weather_data["currentConditions"]["temp"]["c"]
	icon 			= weather_data["currentConditions"]["iconURL"]

	data = {
		"location"	: location,
		"temp" 		: temp,
		"icon"		: icon
	}

	return render_template('index.html', data=data)