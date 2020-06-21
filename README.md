# Final Project
(By Mingxuan Chen, Squad C)

Simple flask server that returns exchange rates, covid-19 cases and public holidays via python module. 

## To Build

Ensure you have:

* **python3**

### Install

```
pip install flask --user
pip install yfinance --user
pip install json2html
```

## Instrcutions 
### First Endpoint (returns json)
This returns a simple JSON object with exchange rates from your base currency to other currencies.
(e.g.CAD, CNY, EUR, GBP, HKD, JPY, USD...)
The endpoint is: /exchangerate/currency/<your base currency>.json

### Seond Endpoint (returns html)
This reutrns a HTML object with confirmed cases for a country for a specific time period.
(Country examples: United States, United Kindom, Italy, Cananda, Switzerland...)
*Note: Date format should be YYYY-MM-DD
The endpoint is: /covid19/country/<country you want to check>/from/<start date>/to/<end date>.html

### Third Endpoint (returns html)
This reutrns a HTML object with public holidays from a given year and country.
(Countrycode examples: CA, CN, DE, FR, GB, US... )
The endpoint is: /publicholidays/year/<year you want to check>/countrycode/<countrycode you want to check>.html

## To Run

```
python3 -m main
```

(Ctrl + C to quit)

## To Use

Go to your browser, type in `http://127.0.0.1:5000` into your browser and add endpoints as defined in code.
