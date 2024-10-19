# To install flask, first run the following line in the terminal:
# pip install flask
# pip install python-dotenv

from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os
flask_app = Flask(__name__)

load_dotenv()

db_username = os.environ["MONGODB_USERNAME"]
db_password = os.environ.get("MONGODB_PASSWORD")

# MongoDB Atlas Connection
client = MongoClient(f"mongodb+srv://{db_username}:{db_password}@cluster0.bb9ww.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.shop_db
products_collection = db.products

from app import routes
