from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request
import sys
import json
from geoalchemy2 import Geometry
from flask import jsonify
from shapely import wkb
import shapely.geometry
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:master@localhost:5432/world_pop'
db = SQLAlchemy()
db.init_app(app)

class Countries(db.Model):
    __tablename__ = 'world_population'
    Country = db.Column(db.Integer, unique=True, nullable=False,primary_key=True)
    Population = db.Column(db.Integer())
    Yearly_Change = db.Column(db.Integer())
    Net_Change = db.Column(db.Float())
    Density = db.Column(db.Integer())
    Land_Area = db.Column(db.Integer())
    Migrants = db.Column(db.Integer())
    Fert_Rate = db.Column(db.Float())
    Mid_Age = db.Column(db.Integer())
    Urban_pop = db.Column(db.Float())
    World_Share = db.Column(db.Float())

    def __init__(self, Country, Population, Yearly_Change, Net_Change, Density, Land_Area, Migrants, Fert_Rate, Mid_Age, Urban_pop, World_Share):
        self.Country = Country
        self.Population = Population
        self.Yearly_Change = Yearly_Change
        self.Net_Change = Net_Change
        self.Density = Density
        self.Land_Area = Land_Area
        self.Migrants = Migrants
        self.Fert_Rate = Fert_Rate
        self.Mid_Age = Mid_Age
        self.Urban_pop = Urban_pop
        self.World_Share = World_Share

    def __repr__(self):
        return f"<result {self.Country}>"

class Polygons(db.Model):
    __tablename__ = 'countriespolygon'
    id = db.Column(db.Integer, unique=True, nullable=False,primary_key=True)
    iso3 = db.Column(db.String())
    status = db.Column(db.String())
    color_code = db.Column(db.String())
    name = db.Column(db.String())
    continent = db.Column(db.String())
    region = db.Column(db.String())
    iso_3166_1 = db.Column(db.String())
    french_sho = db.Column(db.String())
    geometry = db.Column(Geometry("POLYGON"))

    def __init__(self, id, iso3, status, color_code, name, continent, region, iso_3166_1, french_sho, geometry, World_Share):
        self.id = id
        self.iso3 = iso3
        self.status = status
        self.color_code = color_code
        self.name = name
        self.continent = continent
        self.region = region
        self.iso_3166_1 = iso_3166_1
        self.french_sho = french_sho
        self.geometry = geometry

    def __repr__(self):
        return f"<result {self.name}>"
    


@app.get('/initialize')
def initialize():
    countries = []
    with open('data.json') as f:
        countries = json.load(f)
        print(countries,file=sys.stdout)
    for c in countries:
        print(c)
        country = Countries(
            Country=c['Country'],
            Population=c['Population'],
            Yearly_Change=c['Yearly Change'],
            Net_Change=c['Net Change'],
            Density=c['Density'],
            Land_Area=c['Land Area'],
            Migrants=c['Migrants'],
            Fert_Rate=c['Fert Rate'],
            Mid_Age=c['Mid Age'],
            Urban_pop=c['Urban pop'],
            World_Share=c['World Share'],
        )
        db.session.add(country)
    db.session.commit()

@app.get('/countries/<name>')
def get_countries(name):
    country = Countries.query.filter_by(Country=name).first()
    polygon = Polygons.query.filter_by(name=name).first()
    js = shapely.geometry.mapping(wkb.loads(bytes(polygon.geometry.data)))
    gjs = {
        "type":"Feature",
        "geometry":js,
        "properties":{
            "population": country.Population, 
            "Density": country.Density,
            "Yearly_Change": country.Yearly_Change,
            "Mid_Age": country.Mid_Age,
            "Migrants": country.Migrants,
            "World_Share": country.World_Share,
        }
        
    }
    return jsonify(gjs)

@app.get('/countries/<all>')
def get_world_population():
    conn = sqlite3.connect('world_pop.db')
    c = conn.cursor()
    c.execute("SELECT * FROM world_population")
    results = c.fetchall()
    conn.close()
    return jsonify(results)


@app.route('/')
def hello():
    return render_template('country.html')    

if __name__ == "__main__":
    
    with app.app_context():
          db.create_all()
    app.run(host='0.0.0.0',port=80)