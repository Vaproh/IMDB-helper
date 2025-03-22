# IMDb Helper 📽️🎬

## Overview ✨
IMDb Helper is a Python library that provides an easy way to interact with IMDb data using the IMDbPY library. It allows users to search for movies, retrieve IMDb IDs, and fetch detailed information such as title, rating, cast, director, and genres.

## Features 🚀
- Search for movies by name 🔍
- Retrieve IMDb ID for a given movie 🆔
- Fetch detailed movie information, including title, rating, genres, cast, and director 🎭
- Simple and easy-to-use interface ⚡

## Installation 💻
### Requirements
- Python 3.x 🐍
- `imdbpy` library 📚

### Install Dependencies
```sh
pip install IMDbPY
```

## Basic Usage 🎥
### Initialize IMDb Helper
```python
from imdb_helper import IMDbHelper

helper = IMDbHelper()
```

### Search for a Movie 🔎
```python
movies = helper.search_movie("Inception")
for movie in movies[:5]:  # Show top 5 results
    print(f"{movie['title']} ({movie.get('year', 'N/A')})")
```

### Get IMDb ID 🎭
```python
imdb_id = helper.get_imdb_id("Inception")
print(f"IMDb ID: {imdb_id}")
```

### Get Movie Details 🎞️
```python
if imdb_id:
    details = helper.get_movie_details(imdb_id)
    print(f"Title: {details.get('title')}")
    print(f"Year: {details.get('year')}")
    print(f"Rating: {details.get('rating')}")
    print(f"Genres: {', '.join(details.get('genres', []))}")
    print(f"Director(s): {', '.join([d['name'] for d in details.get('director', [])])}")
    print(f"Top Cast: {', '.join([c['name'] for c in details.get('cast', [])[:5]])}")
```

For more details, refer to the [documentation](./documentation.md) 📖.

## License 📜
This project is open-source and available under the MIT License.

## Disclaimer ⚠️
This project is for educational purposes only. Ensure compliance with IMDb's terms of service when using this library.


