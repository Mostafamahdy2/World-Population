# World Population Search

This web page presents the final project for the 2023 Erasmus Master in Geospatial Technologies programming course as part of the Geolocation Advancement. The main goal is to create a webpage that helps the user to query information about the population in all countries of the world and Provide him with a ready-to-use GeoJSON map to suit his needs.

## Requirements
* Python 3, with packages outlined in required_packages.txt
* Packages can be manually downloaded and installed using conda and/or pip.
* Alternatively, use Anaconda Prompt to create a virtual environment (containing the requred packeges) 

```python
Python Packages Used:
    
    numpy
    pandas
    geopandas
    sqlalchemy
    flask
    matplotlib
    requests
    json
    bs4 

```
Languages used:

    Python
    HTML
    CSS
    JavaScript
Javascript Libraries Used:

    
    Leaflet
    jQuery
    


## Database

The data used in this project was extracted from [this link](https://www.worldometers.info/world-population/population-by-country/) 
then started to create our database "World_pop" was created through the use of PGadmin and we used the extension PostGIS to work with the geometries inside the tables. The tables and views used on ETL and API scripts were created using SQL scripts that are inside the database folder to run it in sequencial order. The database has two tables "world_population" for the population data and the other one called "countriespolygon" for the  geometry.

## 



## The output and Visualisation

![Result](https://user-images.githubusercontent.com/126589869/221987584-c243a2b7-f9b5-4bfa-a75c-afc50c7b292c.JPG)

On the front end has been developed a search functions to retrieve the stored data  in the database and show the required information.

![test1](https://user-images.githubusercontent.com/126589869/221990197-de103e56-d3f2-41bb-8076-98698b9d4b11.JPG)
![test2](https://user-images.githubusercontent.com/126589869/221990463-122c3030-e519-4b6f-9ee5-53c86e857ffe.JPG)



