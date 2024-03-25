from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Import and register blueprints
    from app.api.tmdb import api_blueprint
    from app.main import main_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')
    app.register_blueprint(main_blueprint, url_prefix='/')

    return app