from flask import Flask
from flask_pymongo import PyMongo

# Create an instance of the Flask class
app = Flask(__name__)
app.config["SECRET_KEY"] = "ba579b049afa5cddb280f78822c8a62802af308a"

#creating mongodb
import pymongo

conn = "mongodb+srv://imran0511:Imran123@assignment3.9btfr2g.mongodb.net/"   #connecting to pymongo
client = pymongo.MongoClient(conn, serverSelectionTimeoutMS=5000)
db = client.db    #creating our database



from application import routes