from config import Config
from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    @app.after_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8082'  # Adjust the origin as needed
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'  # Add allowed methods
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'  # Add allowed headers
        return response

    # Import and register blueprints
    from app.api.tmdb import api_blueprint
    from app.main import main_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')
    app.register_blueprint(main_blueprint, url_prefix='/')

    return app