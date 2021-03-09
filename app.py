from flask import Flask, render_template, redirect, request
import recommender

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
    return render_template("engine_1.html", movie_title=movie_title, results=results, recommendation1=recommendation1) 

@app.route('/engine_2', methods=['POST'])
def run_algo_2():
    user_id = int(request.form['user_id'])
    full_predictions_df = recommender.full_predictions_df
    movies_df = recommender.movies_df
    ratings_df = recommender.ratings_df
    results_2 = recommender.recommendation_engine_2(full_predictions_df, user_id, movies_df, ratings_df)
    top_rated_movies = recommender.top_rated_movies
    final_recommendations = recommender.final_recommendations
    return render_template("engine_2.html", user_id=user_id, results_2=results_2, top_rated_movies=top_rated_movies, final_recommendations=final_recommendations)
    
if __name__ == '__main__':
    app.run(debug=True)