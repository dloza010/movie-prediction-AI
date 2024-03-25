from flask import Blueprint, jsonify, request
import requests

api_blueprint = Blueprint('tmdb_api', __name__)


@api_blueprint.route('/movies')
def get_movies():
    tmdb_api_key = '8478ea2da772165abc7148ffef0802b6'
    query = request.args.get('query', 'Matrix')
    tmdb_url = f'https://api.themoviedb.org/3/search/movie?api_key={tmdb_api_key}&query={query}'
    response = requests.get(tmdb_url)
    response = jsonify(response.json()['results'])
    response.headers['Access-Control-Allow-Origin'] = '*'
    print(response)
    return response


