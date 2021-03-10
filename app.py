from flask import Flask, render_template, redirect, request
import recommender
import posters
import config

app = Flask(__name__)

@app.route('/')
def index():
    movie_titles = recommender.movie_titles
    return render_template("index.html", movie_titles=movie_titles)

@app.route('/engine_1', methods=['POST'])
def run_algo():
    movie_title = request.form['movie_title']
    results = recommender.recommendation_engine_1(movie_title)
    recommendation1 = recommender.recommendation1
    api_key = config.api_key
    all_posters = posters.get_posters_1(movie_title)
    all_posters_2 = posters.get_posters_2(recommendation1)
    recommendation1_posters = posters.recommendation1_posters
    movie_title_poster = posters.movie_title_poster
    return render_template("engine_1.html", movie_title=movie_title, results=results, recommendation1=recommendation1, 
        all_posters=all_posters, movie_title_poster=movie_title_poster, api_key=api_key, all_posters_2=all_posters_2, recommendation1_posters=recommendation1_posters) 

@app.route('/engine_2', methods=['POST'])
def run_algo_2():
    user_id = int(request.form['user_id'])
    full_predictions_df = recommender.full_predictions_df
    movies_df = recommender.movies_df
    ratings_df = recommender.ratings_df
    results_2 = recommender.recommendation_engine_2(full_predictions_df, user_id, movies_df, ratings_df)
    top_rated_movies = recommender.top_rated_movies
    final_recommendations = recommender.final_recommendations
    random_user = recommender.random_user
    get_posters_3 = posters.get_posters_3(top_rated_movies)
    top_rated_posters = posters.top_rated_posters
    get_posters_4 = posters.get_posters_4(final_recommendations)
    final_recommendations_posters = posters.final_recommendations_posters
    return render_template("engine_2.html", user_id=user_id, random_user=random_user, results_2=results_2, top_rated_movies=top_rated_movies, 
        final_recommendations=final_recommendations, get_posters_3=get_posters_3, top_rated_posters=top_rated_posters, final_recommendations_posters=final_recommendations_posters, 
        get_posters_4=get_posters_4)
    
if __name__ == '__main__':
    app.run(debug=True)