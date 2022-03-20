from flask import Flask, render_template, request
import requests

DEFAULT_LOC = "London"

app 	= Flask(__name__)

@app.route('/')
def home():
	ip	= request.environ.get("HTTP_X_FORWARDED_FOR")
		
	location_request 	= requests.get(f"http://ip-api.com/json/{ip}")
	location_data		= location_request.json()
	if location_data["status"] == "success":
		location = location_data['city']
	else:
		location = DEFAULT_LOC

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
