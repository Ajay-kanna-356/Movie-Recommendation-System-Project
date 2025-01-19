from flask import Flask,render_template,request
import json
from designpatterns import apply_filters_facade
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("home.html")
@app.route("/movies",methods = ['POST'])
def moviepage(): 
    d_name = request.form.get('dname')
    rating = request.form.get('rating')
    genre = request.form.get('genre')
    with open("MovRecSys/movies.json","r") as f:
        movies = json.load(f)
    filtered_movies = apply_filters_facade(movies,genre=genre,rating=rating,director_name=d_name)
    return render_template("moviepage.html",movies = filtered_movies)
if __name__ == "__main__":
    app.run(debug=True)