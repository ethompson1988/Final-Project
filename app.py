from flask import Flask, render_template, redirect
import recommender

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/engine_1')
def engine_1():
    return render_template("engine_1.html", engine_1=recommender.recommendation_engine_1())
    # engine_1 = recommender.recommendation_engine_1()

@app.route('/engine_2')
def engine_2():
    return render_template('engine_2.html', engine_2 = recommender.recommendation_engine_2())
    
    
if __name__ == '__main__':
    app.run(debug=True)