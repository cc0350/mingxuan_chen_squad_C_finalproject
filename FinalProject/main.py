import requests
from json2html import *
from flask import (
	Flask, 
	jsonify,
	request,
	render_template,
	Response,
)

app = Flask(__name__)

# First endpoint (return json)
@app.route('/covid19/CountryInformation.json')
def countries():
	url = f"https://api.covid19api.com/countries"
	countries = requests.get(url)
	countries_json = countries.json()
	return Response(
		countries,
		mimetype = "application/json")

# Second endpoint (return html)
@app.route('/covid19/country/<country>/allcases.html')
def dayone_country_allcases(country):
	url = f"https://api.covid19api.com/total/dayone/country/{country}"
	all_cases = requests.get(url)
	all_cases = all_cases.json()
	all_cases_html = json2html.convert(json = all_cases)
	return render_template("All Cases.html", data = all_cases_html, country = country)


@app.route('/covid19/country/<country>/status/<status>/from/<start>/to/<end>.html')
def country_case_time_period(country,status,start,end):
	url = f"https://api.covid19api.com/total/country/{country}/status/{status}?from={start}T00:00:00Z&to={end}T00:00:00Z"
	today_case = requests.get(url)
	today_case = today_case.json()
	today_case_html = json2html.convert(json = today_case)
	return render_template("Cases for specific timeperiod.html", data = today_case_html, country = country, first_date = start, end_date = end, status = status)

# Third endpoint (return html)
@app.route('/covid19/summary/country/<country>/from/<start>/to/<end>.html')
def summary(country, start, end):
	return render_template("Summary.html", country = country, first_date = start, end_date = end)


if __name__ == '__main__':
	app.run(debug=True)