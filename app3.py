# DEPENDENCIES
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from flask_pymongo import PyMongo
import os
import pymongo

app = Flask(__name__)

# SET UP MONGO DB CONNECTION
app.config['MONGO_DBNAME'] = 'Pets'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Pets'

mongo = PyMongo(app)

#QUERY COLLECTIONS
mainCol = mongo.Main
wheelCol = mongo.Images
shelterCol = mongo.Shelters

# CREATE ROUTES

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/wheel')
def wheel():
    

    return render_template("wheel.html")


@app.route("/shelters")
def shelters():
    return render_template("locations.html")

@app.route("/pie")
def mainData():
    pass

# FINALIZE
if __name__ == "__main__":
    app.run(debug=True)