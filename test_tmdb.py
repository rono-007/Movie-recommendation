import requests

API_KEY = ""  # Replace with your actual TMDb API key
BASE_URL = "https://api.themoviedb.org/3"
genre_id = 28  # Action Genre ID

# Construct API request URL
url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}&sort_by=popularity.desc"

# Fetch data from TMDb API
response = requests.get(url).json()

# Print the response
print(response)
