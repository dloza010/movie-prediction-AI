import requests
from dotenv import load_dotenv
import os

load_dotenv()


class TMDbAPI:
    def __init__(self):
        self.api_key = os.getenv('TMDB_API_KEY')
        self.base_url = 'https://api.themoviedb.org/3'

    def search_movie(self, title):
        search_url = f"{self.base_url}/search/movie"
        params = {'api_key': self.api_key, 'query': title}
        response = requests.get(search_url, params=params)
        response.raise_for_status()
        return response.json().get('results', [])

    def get_movie_details(self, movie_id):
        details_url = f"{self.base_url}/movie/{movie_id}"
        params = {'api_key': self.api_key}
        response = requests.get(details_url, params=params)
        response.raise_for_status()
        return response.json()
