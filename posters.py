import requests
import json
from config import api_key
import recommender

def get_posters_1(movie_title):
    url = f'http://www.omdbapi.com/?t='
    movie_title = movie_title[0:-7]
    response1 = requests.get(url + movie_title + api_key)
    data1 = response1.json()
    global movie_title_poster
    if 'Poster' in data1:
        movie_title_poster = data1['Poster']
    else:
        movie_title = movie_title[0:-12]
        response = requests.get(url + "The " + movie_title + api_key)
        data = response.json()
        if 'Poster' in data:
                movie_title_poster = data['Poster']
    return movie_title_poster

def get_posters_2(recommendation):
    url = f'http://www.omdbapi.com/?t='
    global recommendation1_posters
    recommendation1_posters = []
    for x in range(10):
        movie_title = recommendation[x][0:-7]
        print(movie_title)
        response = requests.get(url + movie_title + api_key)
        data = response.json()
        if 'Poster' in data:
            poster_data = data['Poster']
            recommendation1_posters.append(poster_data)
        else:
            movie_title = recommendation[x][0:-12]
            response = requests.get(url + "The " + movie_title + api_key)
            data = response.json()
            if 'Poster' in data:
                poster_data = data['Poster']
                recommendation1_posters.append(poster_data)
            else:
                recommendation1_posters.append(x)
    return recommendation1_posters

def get_posters_3(rated_movies):
    url = f'http://www.omdbapi.com/?t='
    global top_rated_posters
    top_rated_posters = []
    for x in range(5):
        movie_title = rated_movies[x][0:-7]
        print(movie_title)
        response = requests.get(url + movie_title + api_key)
        data = response.json()
        if 'Poster' in data:
            poster_data = data['Poster']
            top_rated_posters.append(poster_data)
        else:
            movie_title = rated_movies[x][0:-12]
            response = requests.get(url + "The " + movie_title + api_key)
            data = response.json()
            if 'Poster' in data:
                poster_data = data['Poster']
                top_rated_posters.append(poster_data)
            else:
                top_rated_posters.append(x)
    return top_rated_posters

def get_posters_4(recommendations):
    url = f'http://www.omdbapi.com/?t='
    global final_recommendations_posters
    final_recommendations_posters = []
    for x in range(5):
        movie_title = recommendations[x].values[0][0:-7]
        response = requests.get(url + movie_title + api_key)
        data = response.json()
        if 'Poster' in data:
            poster_data = data['Poster']
            final_recommendations_posters.append(poster_data)
        else:
            movie_title = recommendations[x].values[0][0:-12]
            response = requests.get(url + "The " + movie_title + api_key)
            data = response.json()
            if 'Poster' in data:
                poster_data = data['Poster']
                final_recommendations_posters.append(poster_data)
            else:
                final_recommendations_posters.append(x)
        

