from flask import Blueprint, jsonify, request
from ..models.recommendation import hybrid_recommendation
from ..models.tmdb import TMDbAPI

recommendation = Blueprint('recommendation', __name__)
tmdb_api = TMDbAPI()
@recommendation.route('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('user_id', default=1, type=int)
    recommended_titles = hybrid_recommendation(user_id)
    print(recommended_titles)

    movies_info = []
    for title in recommended_titles:
        movie_data = tmdb_api.search_movie(title)
        movie_id = movie_data[0]['id']
        print(movie_id)
        if movie_id:
            movie_details = tmdb_api.get_movie_details(movie_id)
            movies_info.append(movie_details)

    return jsonify(movies_info=movies_info)
