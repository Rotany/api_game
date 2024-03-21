from flask import jsonify, Flask, request
from mongo_client import MongoManager

app = Flask(__name__)

mongo_client = MongoManager("localhost", 27017, "cave_game")

@app.route("/adadaa", methods = ['POST'])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/best-scores", methods=["GET"])
def get_best_scores():
    print(request.data)
    mongo_client.insert_document("hola", {"togu": "hermoso"})
    return jsonify({2: 4})