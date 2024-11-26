from flask import Flask
from flask_pymongo import PyMongo
from .routes.user_routes import user_bp
from .routes.flashcard_routes import flashcards_bp
from config import Config 
import jsonify

# Initialize PyMongo instance globally
mongo = PyMongo()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb+srv://admin:Nora0709<3@crochetbuilder.gld0hso.mongodb.net/flashcard_app?retryWrites=true&w=majority"
    
    # Load configuration
    app.config.from_object(Config)
    mongo = PyMongo(app)

    # Initialize PyMongo
    
    mongo.init_app(app)

     # Register error handlers
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"error": "Bad request", "message": str(error)}), 400

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({"error": "Forbidden", "message": str(error)}), 403

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not found", "message": str(error)}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Internal server error", "message": str(error)}), 500
    
    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(flashcards_bp, url_prefix='/api')

    @app.route('/')
    def home():
        return "Welcome to the homepage!"
    
   
    return app