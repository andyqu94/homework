import datetime
from datetime import date, timedelta
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

app = Flask(__name__)

@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api.v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api.v1.0/precipitation")
def precipitation():

    # Query precipitation
    results = session.query(Measurement).filter(Measurement.date)
    
    prcp_data = []
    for row in results:
        prcp_dict = {}
        prcp_dict[row.date] = row.prcp
        prcp_data.append(prcp_dict)

    return jsonify(prcp_data)

@app.route("/api/v1.0/stations")
def stations():

    # Query stations
    results = session.query(Station)

    station_data = []
    for station in results:
        station_dict = {}
        station_dict["Station"] = station.station
        station_dict["Name"] = station.name
        station_data.append(station_dict)

    return jsonify(station_data)

@app.route("/api/v1.0/tobs")
def tobs():

    # Query temperatures
    results = session.query(Measurement).filter(Measurement.date)

    temp_data = []
    for row in results:
        temp_dict = {}
        temp_dict[row.date] = row.tobs
        temp_data.append(temp_dict)

    return jsonify(temp_data)

@app.route("/api/v1.0/<start>")
def start_date(start_date):

    results = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).filter(Measurement.date >= start_date).all()

    return jsonify({"Min Temp": results[0][0], "Avg Temp" : results[0][1],"Max Temp" : results[0][2]})

@app.route("/api/v1.0/<start>/<end>")
def date_between(start_date, end_date):

     results = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).filter(Measurement.date >= start_date, Measurement.date <= end_date).all()
     
     return jsonify({"Min Temp": results[0][0], "Avg Temp" : results[0][1],"Max Temp" : results[0][2]})

if __name__ == '__main__':
    app.run(debug=True)