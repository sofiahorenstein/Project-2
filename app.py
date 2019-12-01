from flask import Flask, jsonify, render_template
from flask_pymongo import PyMongo
import petapi
import requests
import json 
import os
import pandas as pd 


app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo_password = os.environ['MONGODB_PASSWORD']
mongo_connection_string = f"mongodb+srv://sofiahorenstein:{mongo_password}@cluster0-lursa.mongodb.net/test?retryWrites=true&w=majority"

# app.config["MONGO_URI"] = "mongodb://localhost:27017/petfinder_app"
app.config["MONGO_URI"] = mongo_connection_string
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/api/<breed>")
def get_pets_by_breed(breed):
    pets = mongo.db.pets.find({"breed": breed})
    return jsonify(pets)
#create endpoint to update the data (like scrape)

@app.route("/update")
def update():
    pets = mongo.db.pets
    pet_data = petapi.get_pets(10)
    pets.update({}, {"pets": pet_data}, upsert=True)
    return jsonify(pet_data)

@app.route("/")
def index(): 
    # write a statement that finds all the items in the db and sets it to a variable
    current_pet_data = mongo.db.pets.find()
    print(current_pet_data)

    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", current_pet_data=current_pet_data)

    
@app.route('/wheel')
def wheel():
    return render_template("wheel2.html")


@app.route("/shelters")
def shelters():
    return render_template("locations.html")

@app.route("/pie")
def mainData():
    pass


if __name__ == "__main__":
    app.run(debug=True)