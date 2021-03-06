# %matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Import movies csv
movies_df = pd.read_csv('data/movies.csv')
# movies_df.head()
# len(movies_df)

#Import ratings csv
ratings_df = pd.read_csv('data/ratings.csv', parse_dates=['timestamp'])
ratings_df = ratings_df.drop(columns=['timestamp'])
# ratings_df.head()

#Combine 'movies' and 'ratings' dataframes and drop timestamp column
combined_df = pd.merge(ratings_df, movies_df, how='right', on='movieId')
# combined_df = combined_df.drop(columns=['timestamp'])
# combined_df

#Extract a list of individual genres from 'genres' column in df
genres_list = []
unique_genres = []
for genre in combined_df.genres.unique():
    genres_list.append(genre)
for x in range(len(genres_list)):
    genres_list[x] = genres_list[x].split('|')
for x in genres_list:
    for genre in x:
        if genre not in unique_genres:
            unique_genres.append(genre)
# unique_genres

all_genres = []
for x in movies_df['genres']:
    all_genres.append(x)
# all_genres

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_model = TfidfVectorizer(analyzer='word',stop_words='english')
tfidf_values = tfidf_model.fit_transform(movies_df['genres'])
# tfidf_values.shape

from sklearn.metrics.pairwise import linear_kernel
cosine_sim = linear_kernel(tfidf_values, tfidf_values)
# cosine_sim.shape

movie_titles = np.array(movies_df['title'])
def recommendation_engine_1(movie_title):
    for x in range(len(movie_titles)):
        if movie_titles[x] == movie_title:
            index = x
            similarity = list(enumerate(cosine_sim[index]))
    similarity = sorted(similarity, key=lambda x: x[1], reverse=True)
    similarity = similarity[1:11]
    movie_indices = [i[0] for i in similarity]
    global recommendation1
    recommendation1 = movie_titles[movie_indices]    
    return recommendation1

print(f"Because you liked Jumanji, we recommend the following movies: \n{recommendation_engine_1('Jumanji (1995)')}")

#Turn df into matrix with users as rows and movies as columns
collab_df = ratings_df.pivot(index = 'userId', columns ='movieId', values = 'rating').fillna(0)
collab_matrix = collab_df.to_numpy()
# print(collab_matrix)
#Normalize data
user_ratings_mean = np.mean(collab_matrix, axis = 1)
normalized_matrix = collab_matrix - user_ratings_mean.reshape(-1, 1)
# normalized_matrix

from scipy.sparse.linalg import svds
U, sigma, Vt = svds(normalized_matrix, k = 200)
sigma = np.diag(sigma)
all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)
full_predictions_df = pd.DataFrame(all_user_predicted_ratings, columns = collab_df.columns)
# full_predictions_df

def recommendation_engine_2(full_predictions_df, userId, movies_df, ratings_df):
    
    user_predictions_df = full_predictions_df.iloc[userId - 1].sort_values(ascending=False)
    user_ratings_df = ratings_df[ratings_df.userId == (userId)]
    user_full = (user_ratings_df.merge(movies_df, how = 'left', left_on = 'movieId', right_on = 'movieId').
                     sort_values(['rating'], ascending=False))
    top_rated_movies = user_full['title'].to_list()
    recommended_movie_ids = user_predictions_df.index
    already_rated_ids = user_ratings_df['movieId'].to_list()
    final_recommendations = []
    for x in recommended_movie_ids:
        if x not in already_rated_ids:
            final_recommendations.append(movies_df.loc[movies_df['movieId']==x]['title'])
    
    return f"UserID {userId} ",top_rated_movies[0:10], final_recommendations[0:5]

from numpy import random
random_user = np.random.randint(0,high=668)
# recommendation_engine_2(full_predictions_df, 501, movies_df, ratings_df)