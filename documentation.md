# IMDb Helper Documentation

## Overview
IMDb Helper is a Python library that provides an easy way to interact with IMDb data using the IMDbPY library. This documentation covers all available functions with explanations and examples.

## Installation
### Requirements
- Python 3.x
- `imdbpy` library

### Install Dependencies
```sh
pip install IMDbPY
```

## Class: `IMDbHelper`
This class provides methods to interact with IMDb data, such as searching for movies, retrieving IMDb IDs, and fetching movie details.

### **`__init__()`**
Initializes the IMDbHelper class by creating an instance of the IMDb class.
```python
helper = IMDbHelper()
```

### **`search_movie(movie_name)`**
Searches for movies by name and returns a list of matching movies.

#### **Arguments:**
- `movie_name` (str): The name of the movie to search for.

#### **Returns:**
- `list`: A list of movie objects matching the search query.

#### **Example:**
```python
movies = helper.search_movie("Inception")
for movie in movies[:5]:
    print(f"{movie['title']} ({movie.get('year', 'N/A')})")
```

### **`get_imdb_id(movie_name)`**
Retrieves the IMDb ID of the first matching movie from the search results.

#### **Arguments:**
- `movie_name` (str): The name of the movie.

#### **Returns:**
- `str`: The IMDb ID of the movie, or None if no match is found.

#### **Example:**
```python
imdb_id = helper.get_imdb_id("Inception")
print(f"IMDb ID: {imdb_id}")
```

### **`get_movie_details(imdb_id)`**
Retrieves detailed information about a movie using its IMDb ID.

#### **Arguments:**
- `imdb_id` (str): The IMDb ID of the movie.

#### **Returns:**
- `dict`: A dictionary containing movie details such as title, year, rating, genres, cast, and director.

#### **Example:**
```python
details = helper.get_movie_details(imdb_id)
print(details)
```

### **`get_movie_title(imdb_id)`**
Retrieves the title of a movie using its IMDb ID.

#### **Arguments:**
- `imdb_id` (str): The IMDb ID of the movie.

#### **Returns:**
- `str`: The title of the movie, or None if not available.

#### **Example:**
```python
title = helper.get_movie_title(imdb_id)
print(f"Title: {title}")
```

### **`get_movie_rating(imdb_id)`**
Retrieves the IMDb rating of a movie.

#### **Arguments:**
- `imdb_id` (str): The IMDb ID of the movie.

#### **Returns:**
- `float`: The IMDb rating, or None if not available.

#### **Example:**
```python
rating = helper.get_movie_rating(imdb_id)
print(f"Rating: {rating}")
```

### **`get_movie_cast(imdb_id, max_cast=5)`**
Retrieves the top cast members of a movie.

#### **Arguments:**
- `imdb_id` (str): The IMDb ID of the movie.
- `max_cast` (int, optional): Maximum number of cast members to return (default: 5).

#### **Returns:**
- `list`: A list of top cast members.

#### **Example:**
```python
cast = helper.get_movie_cast(imdb_id)
print(f"Top Cast: {', '.join([c['name'] for c in cast])}")
```

### **`get_movie_director(imdb_id)`**
Retrieves the director(s) of a movie.

#### **Arguments:**
- `imdb_id` (str): The IMDb ID of the movie.

#### **Returns:**
- `list`: A list of directors.

#### **Example:**
```python
directors = helper.get_movie_director(imdb_id)
print(f"Director(s): {', '.join([d['name'] for d in directors])}")
```

### **`get_movie_genres(imdb_id)`**
Retrieves the genres of a movie.

#### **Arguments:**
- `imdb_id` (str): The IMDb ID of the movie.

#### **Returns:**
- `list`: A list of genres.

#### **Example:**
```python
genres = helper.get_movie_genres(imdb_id)
print(f"Genres: {', '.join(genres)}")
```

## License
This project is open-source and available under the MIT License.

## Disclaimer
This project is for educational purposes only. Ensure compliance with IMDb's terms of service when using this library.


