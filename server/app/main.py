from flask import Blueprint, jsonify

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def home():
    return jsonify({'message': 'Welcome to the Movie Server'})
