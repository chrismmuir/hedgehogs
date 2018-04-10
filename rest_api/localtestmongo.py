from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import requests

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'mydb'
app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017'

mongo = PyMongo(app)


@app.route('/movie', methods=['GET'])
def get_all_inputs():
    inputs = mongo.db.movie
    output = []
#     for q in fin_data.find():
#         output.append(q.name)
    return jsonify({'result' : output})
# def hello():
# 	return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)