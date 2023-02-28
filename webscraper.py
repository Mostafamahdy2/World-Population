import numpy as np
import pandas as pd
import matplotlib as plt
import requests
import json
from bs4 import BeautifulSoup as bs

url = 'https://www.worldometers.info/world-population/population-by-country/'
response = requests.get(url)
print(response.status_code)

soup = bs(response.text, 'html.parser')

table = soup.find_all('table', class_ = 'table')

def testNA(data):
    if data == "N.A.":
        return "0"
    elif " %" in data:
        return data[:-2]
    elif "," in data:
        return data.replace(",","")
    elif data == " ":
        return "0"
    else:
        return data

for world_population in table[0].find_all('tbody'):
   rows = world_population.find_all('tr')
   world_population = []
for row in rows:
    Country = row.find_all('td')[1].text
    Population = int(testNA(row.find_all('td')[2].text))
    Yearly_Change = float(testNA(row.find_all('td')[3].text))
    Net_Change = int(testNA(row.find_all('td')[4].text))
    Density = int(testNA(row.find_all('td')[5].text))
    Land_Area = int(testNA(row.find_all('td')[6].text))
    Migrants = int(testNA(row.find_all('td')[7].text))
    Fert_Rate = float(testNA(row.find_all('td')[8].text))
    Mid_Age = int(testNA(row.find_all('td')[9].text))
    Urban_pop = float(testNA(row.find_all('td')[10].text))
    World_Share = float(testNA(row.find_all('td')[11].text))
    world_population.append({
        'Country': Country,
        'Population': Population,
        'Yearly Change': Yearly_Change,
        'Net Change': Net_Change,
        'Density': Density,
        'Land Area': Land_Area,
        'Migrants' : Migrants,
        'Fert Rate' : Fert_Rate,
        'Mid Age' : Mid_Age,
        'Urban pop' : Urban_pop,
        'World Share' : World_Share,
    })

with open('data.json', 'w') as json_file:
   json.dump(world_population, json_file, indent=3)

df_data=pd.DataFrame(world_population)


