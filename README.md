# Final Project
(By Mingxuan Chen, Squad C)

Simple flask server that returns covid-19 related information via python module. 

## To Build

Ensure you have:

* **python3**

### Install

```
pip install flask --user
pip install requests --user
pip install json2html
```

## Instrcutions 
### First Endpoint (returns json)
Returns all the available countries and provinces, as well as the country slug for per country requests.

The endpoint is: /covid19/CountryInformation.json

### Seond Endpoint (returns html)
Returns all cases by case type for a country from the first recorded case. 

(Country examples: United States, United Kindom, Italy, Cananda, Switzerland...) You can also refer to the first endpoint. 

The endpoint is: /covid19/country/{input country}/allcases.html

### Third Endpoint (returns html)
Returns summary by case types for a country during a specific time period.

(Country examples: United States, United Kindom, Italy, Cananda, Switzerland...) You can also refer to the first endpoint. 

*Note: Date format should be YYYY-MM-DD

The endpoint is: /covid19/summary/country/{input country}/from/{input start date}/to/{input end date}.html

## To Run

```
python -m main
```

(Ctrl + C to quit)

## To Use

Go to your browser, type in `http://127.0.0.1:5000` into your browser and add endpoints as defined in code.
