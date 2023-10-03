from flask import Flask, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

mongodb_password = os.environ.get("MONGODB_PW")
mongodb_uri = os.environ.get("MONGODB_URI")

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Connect to MongoDB and fetch data
    client = MongoClient(mongodb_uri)
    db = client['DR3Test']
    collection = db['RegionalDistricts']
    data = list(collection.find({}, {'_id': 0}))

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)