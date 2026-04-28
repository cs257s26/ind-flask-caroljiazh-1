from flask import Flask
import sys
import os


sys.path.insert(0, os.path.dirname(__file__))
from ProductionCode.command_line import load_data, get_country_literacy_growth, get_country_average_year_schooling

app = Flask(__name__)
load_data()


@app.route('/literacy-growth/<country>')


def literacy_rate(country):
   '''Returns the literacy growth report for a given country.
   Route parameter:
    country (str): The name of the country.

    For example to find the literacy rate for France, enter http://127.0.0.1:PORT/literacy-growth/France
   '''
   country_name = country.replace('-', ' ')
   result = get_country_literacy_growth(country_name)


   return result




@app.route('/schooling/<country>/<int:start_year>/<int:end_year>')
def average_education(country, start_year, end_year):
   '''Returns average years of schooling for a country within a year range.
   Route parameters:
    country (str): The name of the country.
    start_year (int): The start year.
    end_year (int): The end year.


   For example to find the stats for France in years between 2000 to 2005, enter http://127.0.0.1:PORT/schooling/France/2000/2020
   '''
   if start_year > end_year:
       return "Please input approriate year range."
  
   country_name = country.replace('-', ' ')


   data = get_country_average_year_schooling(country_name, start_year, end_year)


   if not data:
       return f"No schooling data found for '{country_name}' between {start_year} and {end_year}."
  
   result = f"Average years of schooling in {country_name}:\n"

   for row in data:
       result += f"  {row['year']}: {row['avg_schooling']} years\n"
   
   return result


if __name__ == '__main__': 
   if len(sys.argv) != 2:
       print("Usage: python3 app.py <port>")
       sys.exit(1)
    
   app.run(port=int(sys.argv[1]))