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
@app.route('/exchangerate/currency/<currency>.json')
def exchangerate(currency):
	url = f"https://v6.exchangerate-api.com/v6/9d73873d247a3ab65a8a881c/latest/{currency}"
	rate = requests.get(url)
	rate_json = rate.json()
	return Response(
		rate,
		mimetype = "application/json")

# Second endpoint (return html)
@app.route('/covid19/country/<country>/from/<start>/to/<end>.html')
def today_country_confirmed_case(country,start,end):
	url = f"https://api.covid19api.com/total/country/{country}/status/confirmed?from={start}T00:00:00Z&to={end}T00:00:00Z"
	today_case = requests.get(url)
	today_case = today_case.json()
	today_case_html = json2html.convert(json = today_case)
	return render_template("Covid19.html", data = today_case_html, country = country, first_date = start, end_date = end)

# Third endpoint (return html)
@app.route('/publicholidays/year/<year>/countrycode/<countrycode>.html')
def country_public_holiday(countrycode, year):
	url = f"https://date.nager.at/api/v2/publicholidays/{year}/{countrycode}"
	public_holiday = requests.get(url)
	public_holiday = public_holiday.json()
	public_holiday_html = json2html.convert(json = public_holiday)
	return render_template("Publicholiday.html", data = public_holiday_html, countrycode = countrycode, year = year)



if __name__ == '__main__':
	app.run(debug=True)

	