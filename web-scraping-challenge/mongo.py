from flask import Flask, render_template
from flask_pymongo import PyMongo
import mission_to_mars

app = Flask(__name__)

conn = 'mongodb://localhost:27017'
mongo = Pymongo.MongoClient(conn)

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrapper():
    mars = mongo.db.mars
    mars_data = mission_to_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    return "Scraping Successful"

if __name__ == "__main__":
    app.run()