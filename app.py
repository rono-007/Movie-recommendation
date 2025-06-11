from flask import Flask, render_template, request, session, redirect, url_for
import requests
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Required for session to work

# TMDb API Configuration
API_KEY = ("")
BASE_URL = ""

# Genre dictionary
genre_dict = {
    "Action": 28, "Adventure": 12, "Animation": 16, "Comedy": 35, "Crime": 80,
    "Documentary": 99, "Drama": 18, "Family": 10751, "Fantasy": 14, "History": 36,
    "Horror": 27, "Music": 10402, "Mystery": 9648, "Romance": 10749, "Science Fiction": 878,
    "TV Movie": 10770, "Thriller": 53, "War": 10752, "Western": 37
}

def get_movie_trailer(movie_id):
    """Fetch the YouTube trailer URL for a given movie ID."""
    url = f"{BASE_URL}/movie/{movie_id}/videos?api_key=b43c0697f9fbbcb2771c1ba1f0d1ad97"
    try:
        response = requests.get(url)
        response.raise_for_status()
        videos = response.json().get("results", [])
        trailer = next(
            (f"https://www.youtube.com/embed/{video['key']}"
             for video in videos
             if video["type"] == "Trailer" and video["site"] == "YouTube"),
            None
        )
        return trailer
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch trailer for movie ID {movie_id}: {e}")
        return None

def get_movies_by_genre(genre_name):
    genre_id = genre_dict.get(genre_name)
    if not genre_id:
        return []
    url = f"{BASE_URL}/discover/movie?api_key=b43c0697f9fbbcb2771c1ba1f0d1ad97&with_genres={genre_id}&sort_by=popularity.desc"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        movies = []
        for movie in data["results"][:20]:
            trailer = get_movie_trailer(movie["id"])
            movies.append({
                "id": movie["id"],
                "title": movie["title"],
                "poster": f"https://image.tmdb.org/t/p/w500{movie.get('poster_path', '')}",
                "release_date": movie.get("release_date", "Unknown"),
                "overview": movie.get("overview", "No description available."),
                "trailer": trailer,
                "rating": movie.get("vote_average", None)
            })
        return movies
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return []

def get_top_rated_movies():
    """Fetch the top 100 movies sorted by rating from TMDb."""
    url = f"{BASE_URL}/movie/top_rated?api_key=b43c0697f9fbbcb2771c1ba1f0d1ad97&language=en-US"
    movies = []
    page = 1
    while len(movies) < 100:
        try:
            response = requests.get(f"{url}&page={page}")
            response.raise_for_status()
            data = response.json()
            for movie in data["results"]:
                if len(movies) >= 100:
                    break
                trailer = get_movie_trailer(movie["id"])
                movies.append({
                    "id": movie["id"],
                    "title": movie["title"],
                    "poster": f"https://image.tmdb.org/t/p/w500{movie.get('poster_path', '')}",
                    "release_date": movie.get("release_date", "Unknown"),
                    "overview": movie.get("overview", "No description available."),
                    "rating": movie.get("vote_average", None),
                    "trailer": trailer
                })
            page += 1
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch top rated movies: {e}")
            break
    return movies

def get_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}?api_key=b43c0697f9fbbcb2771c1ba1f0d1ad97&append_to_response=videos"
    try:
        response = requests.get(url)
        response.raise_for_status()
        movie = response.json()
        trailer = next(
            (f"https://www.youtube.com/embed/{video['key']}"
             for video in movie.get("videos", {}).get("results", [])
             if video["type"] == "Trailer" and video["site"] == "YouTube"),
            None
        )
        print(f"Trailer URL for movie ID {movie_id}: {trailer}")
        imdb_id = movie.get("imdb_id")
        reviews = f"https://www.imdb.com/title/{imdb_id}/reviews" if imdb_id else None
        return {
            "title": movie.get("title", "Unknown"),
            "poster": f"https://image.tmdb.org/t/p/w500{movie.get('poster_path', '')}",
            "release_date": movie.get("release_date", "Unknown"),
            "overview": movie.get("overview", "No description available."),
            "rating": movie.get("vote_average", None),
            "trailer": trailer,
            "reviews": reviews
        }
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch movie details: {e}")
        return {
            "title": "Unknown",
            "poster": "",
            "release_date": "Unknown",
            "overview": "No description available.",
            "rating": None,
            "trailer": None,
            "reviews": None
        }

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        genre = request.form.get("genre")
        if genre == "Top 100 Movies":
            movies = get_top_rated_movies()
            session["last_genre"] = genre  # Store the last selected option
            return render_template("results.html", genre="Top 100 Movies", movies=movies, show_rating=True)
        elif genre in genre_dict:
            movies = get_movies_by_genre(genre)
            session["last_genre"] = genre  # Store the last selected genre
            return render_template("results.html", genre=genre, movies=movies, show_rating=False)
    return render_template("index.html", genres=genre_dict.keys())

@app.route("/movie/<int:movie_id>")
def movie_details_route(movie_id):
    details = get_movie_details(movie_id)
    return render_template("movie.html", details=details)

@app.route("/go-back")
def go_back():
    last_genre = session.get("last_genre")
    if last_genre == "Top 100 Movies":
        movies = get_top_rated_movies()
        return render_template("results.html", genre="Top 100 Movies", movies=movies, show_rating=True)
    elif last_genre in genre_dict:
        movies = get_movies_by_genre(last_genre)
        return render_template("results.html", genre=last_genre, movies=movies, show_rating=False)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)