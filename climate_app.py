# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 17:37:38 2020

@author: muthukumar
"""

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from sqlalchemy.pool import QueuePool



#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite",poolclass=QueuePool)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
#Initiate the flask app
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
#home route
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )
@app.route('/api/v1.0/precipitation')
def precipitation():
    session = Session(engine)
    q = [Measurement.date,Measurement.prcp]
    q_result = session.query(*q).all()
    session.close()
    precipitation = []
    for dt, pr in q_result:
        prcp_dict = {}
        prcp_dict["Date"] = dt
        prcp_dict["Precipitation"] = pr
        precipitation.append(prcp_dict)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port = 5000,debug=True)
