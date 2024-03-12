from flask import Flask
from flask_pymongo import PyMongo

def create_mongo_connection():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://mongo:27017/mydatabase"
    mongo = PyMongo(app)
    return mongo

mongo = create_mongo_connection()