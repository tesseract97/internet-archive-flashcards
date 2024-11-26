from flask import current_app, Blueprint, jsonify
from flask_pymongo import PyMongo

flashcards_bp = Blueprint('flashcards', __name__)

@flashcards_bp.route('/flashcards', methods=['GET'])
def find():
    mongo = PyMongo(current_app)
    if mongo.db is None:
        return jsonify({"message": "Database connection unsuccessful"}), 500

    result = mongo.db.flashcards.find_one({"fr": "salut"})
    
    if result:
        return jsonify({"fr": result.get("fr"), "en": result.get("en")})
    else:
        return jsonify({"error": "No matching flashcard found."}), 404
