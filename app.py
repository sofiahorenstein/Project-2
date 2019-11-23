from flask import Flask, jsonify
from flask_pymongo import PyMongo
import petapi

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/petfinder_app"
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

if __name__ == "__main__":
    app.run(debug=True)

