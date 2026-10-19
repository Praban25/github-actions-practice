import os
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

mongo_uri = os.getenv("MONGO_URI", "mongodb://mongo:27017/testdb")
client = MongoClient(mongo_uri)
db = client.testdb

@app.route('/')
def hello():
    db.visits.insert_one({"visitor": "guest"})
    count = db.visits.count_documents({})
    return f"Hello from Docker Compose! Total visits in MongoDB: {count}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
