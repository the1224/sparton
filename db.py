from pymongo import MongoClient
import certifi
ca = certifi.where()

client = MongoClient("mongodb+srv://test:GRMXoJeXQ1CamOqS@cluster0.y2oldeo.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.vote