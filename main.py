from flask import jsonify, Flask, request
from flask_cors import CORS
from mongo.mongo_client import MongoManager
from mongo.entities import User, FinalScore, Points
from mongo.models import UserModel, FinalScoreModel, PointsModel
from mongo.utils import document_to_user, document_to_final_score, document_to_points
import datetime
from bson import ObjectId
import os

app = Flask(__name__)
CORS(app)

mongo_client = MongoManager(
    os.environ.get("MONGO_URL"),
    os.environ.get("MONGO_PORT"),
    "thecavebd"
    )

@app.route("/", methods=["GET"])
def home():
    return jsonify({"msg": "success"})

@app.route("/best-scores", methods=["GET"])
def get_best_scores():
    best_scores = mongo_client.list_best_scores(10)
    best_scores = [document_to_final_score(best_score) for best_score in best_scores]
    return jsonify({"best_scores": best_scores})


@app.route("/users", methods=["GET"])
def get_users():
    users = mongo_client.list_documents("users", {}, False)
    users = [document_to_user(user) for user in users]
    return jsonify({"users": users})


@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    if not data.get("email"):
        return jsonify({"msg": "email is required"}), 400
    if not data.get("password"):
        return jsonify({"msg": "password is required"}), 400
    if not data.get("username"):
        return jsonify({"msg": "username is required"}), 400
    

    user_created = User(data["email"], data["password"], data["username"])
    user_model = UserModel(user_created)
    user_id = mongo_client.insert_document("users", user_model.to_dict())
    return jsonify({"msg": "User created successfully", "user_id": str(user_id)})

@app.route("/final-scores", methods=["POST"])
def create_final_score():
    data = request.json
    if not data.get("user_id"):
        return jsonify({"msg": "user_id is required"}), 400
    if not data.get("score"):
        return jsonify({"msg": "score is required"}), 400

    find_user = mongo_client.list_documents("users", {
        "_id": ObjectId(data["user_id"])}, True
    )
    if not find_user:
        return jsonify({"msg": "User not found"}), 404

    final_score_created = FinalScore(data["user_id"], data["score"])
    final_score_model = FinalScoreModel(final_score_created)
    final_score_id = mongo_client.insert_document("final_scores", final_score_model.to_dict())
    return jsonify({"msg": "Final score created successfully", "final_score_id": str(final_score_id)}), 200

@app.route("/points", methods=["POST"])
def get_points():
    data = request.json
    if not data.get("email"):
        return jsonify({"msg": "email is required"}), 400
    points = mongo_client.list_points(data["email"],10)
    points = [document_to_points(point) for point in points]
    return jsonify({"points": points})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    usuario = data.get('username')
    contrasena = data.get('password')
    is_valid = mongo_client.validar_usuario(usuario,contrasena)
    return jsonify({"is_valid": is_valid})


@app.route("/points", methods=["POST"])
def create_point():
    data = request.json
    if not data.get("user_id"):
        return jsonify({"msg": "user_id is required"}), 400
    if not data.get("coins"):
        return jsonify({"msg": "coins is required"}), 400
    if not data.get("level"):
        return jsonify({"msg": "level is required"}), 400
    if not data.get("hearts"):
        return jsonify({"msg": "hearts is required"}), 400

    find_user = mongo_client.list_documents("users", {
        "_id": ObjectId(data["user_id"])}, True
    )
    if not find_user:
        return jsonify({"msg": "User not found"}), 404

    points = Points(data["user_id"], data["coins"], data["level"], datetime.datetime.now(), data["hearts"])
    point_model = PointsModel(points)

    point_id = mongo_client.insert_document("points", point_model.to_dict())
    return jsonify({"msg": "Point created successfully", "point_id": str(point_id)}), 200

if __name__ == '__main__':
    app.run(debug=True)