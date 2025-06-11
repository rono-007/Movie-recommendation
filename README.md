<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">

</head>
<body>

  <h1>🎬 Movie Recommendation App with TMDb</h1>
  <img src="https://socialify.git.ci/rono-007/Movie-recommendation/image?custom_description=&description=1&font=Source+Code+Pro&name=1&owner=1&pattern=Floating+Cogs&theme=Dark" >

  <p>A Python-based tool that fetches movie data from <strong>The Movie Database (TMDb)</strong> and provides personalized movie recommendations. This project helps you explore and test movie metadata retrieval — ideal for extending into a full recommendation system or web application.</p>

  <hr>

  <h2>📁 Project Structure</h2>
  <pre><code>Movie-recommendation/
├── main.py             # Core logic to fetch and display movie details using TMDb
├── test_tmdb.py        # 🧪 Testing script to validate API key and data fetching
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
</code></pre>

  <hr>

  <h2>⚙️ Installation & Setup</h2>

  <h3>1. Clone the Repository</h3>
  <pre><code>git clone https://github.com/rono-007/Movie-recommendation.git
cd Movie-recommendation</code></pre>

  <h3>2. Set Up a Virtual Environment (Recommended)</h3>
  <pre><code>
    
# For Linux/macOS:
python3 -m venv venv
source venv/bin/activate

# For Windows:
python -m venv venv
venv\Scripts\activate</code></pre>

  <h3>3. Install Python Dependencies</h3>
  <pre><code>pip install -r requirements.txt</code></pre>

  <h3>4. Set Up TMDb API Key</h3>
  <ol>
    <li>Create a <code>.env</code> file in the root folder:</li>
    <pre><code>touch .env</code></pre>
    <li>Add your API key:</li>
    <pre><code>TMDB_API_KEY=your_tmdb_api_key_here</code></pre>
    <li>Get your API key from <a href="https://www.themoviedb.org/documentation/api" target="_blank">TMDb</a>.</li>
  </ol>

  <hr>

  <h2>🚀 How to Run</h2>
  <p>Once you’ve set everything up, run the main script to fetch movie information:</p>
  <pre><code>python main.py</code></pre>

  <p>The script fetches and displays movie data (like The Matrix) including:</p>
  <ul>
    <li>Title</li>
    <li>Overview</li>
    <li>Genres</li>
    <li>Ratings</li>
    <li>Release Date</li>
  </ul>

  <hr>

  <h2>✅ Run Tests</h2>
  <p>To verify if the TMDb API is accessible and functional, run the test script:</p>
  <pre><code>python test_tmdb.py</code></pre>

  <p><strong>Expected Output (on success):</strong></p>
  <pre><code>✔ TMDb fetch successful: The Matrix (1999)</code></pre>

  <p>If there’s an issue with the API key or response, an error message will help debug the problem.</p>

  <hr>

  <h2>🧰 Requirements</h2>
  <p>The project uses the following Python libraries:</p>
  <pre><code>requests
python-dotenv</code></pre>

  <p>Install them using:</p>
  <pre><code>pip install -r requirements.txt</code></pre>

  <hr>

  <h2>🔧 Future Improvements</h2>
  <ul>
    <li>Integrate a real movie recommendation engine (content/collaborative).</li>
    <li>Add a GUI with Streamlit or Flask.</li>
    <li>Filter/search by genre, popularity, release year.</li>
    <li>Add caching or offline fallback.</li>
  </ul>

  <hr>

  <hr>

  <h2>👨‍💻 Author</h2>
  <p>Built by <strong>Ronojoy Nag</strong> — <a href="https://github.com/rono-007" target="_blank">GitHub Profile</a></p>

</body>
</html>
