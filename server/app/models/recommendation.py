import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from .data import df_movies, df_ratings

user_movie_matrix = df_ratings.pivot_table(index='user_id', columns='movie_id', values='rating')

user_similarity = cosine_similarity(user_movie_matrix.fillna(0))

count_vectorizer = CountVectorizer()
count_matrix = count_vectorizer.fit_transform(df_movies['genres'])
movie_similarity = cosine_similarity(count_matrix, count_matrix)


def hybrid_recommendation(user_id, top_n=20):
    try:
        user_profile = user_movie_matrix.loc[user_id]
    except KeyError:
        return "User ID not found in the dataset."

    user_similarity_scores = user_similarity[user_id - 1]
    user_predicted_ratings = user_movie_matrix.T.dot(user_similarity_scores) / user_similarity_scores.sum()

    content_based_scores = movie_similarity.dot(user_profile.fillna(0))

    hybrid_scores = (user_predicted_ratings + content_based_scores) / 2

    sorted_scores = hybrid_scores.sort_values(ascending=False)
    sorted_scores = sorted_scores.drop(user_profile.dropna().index)

    top_movie_indices = sorted_scores.head(top_n).index.tolist()
    recommendations = df_movies[df_movies['id'].isin(top_movie_indices)].title.tolist()

    return recommendations
