from imdb import IMDb


class IMDbHelper:
    """
    A helper class to interact with IMDb data using the IMDbPY library.

    This class provides methods to search for movies, retrieve IMDb IDs,
    and fetch detailed information about movies such as title, rating,
    cast, director, and genres.

    Example usage:
        helper = IMDbHelper()
        imdb_id = helper.get_imdb_id("Inception")
        if imdb_id:
            details = helper.get_movie_details(imdb_id)
            print(details)
    """

    def __init__(self):
        """
        Initializes the IMDbHelper class by creating an instance of the IMDb class.
        """
        self.ia = IMDb()

    def search_movie(self, movie_name):
        """
        Searches for movies by name and returns a list of matching movies.

        Args:
            movie_name (str): The name of the movie to search for.

        Returns:
            list: A list of movie objects matching the search query.
                  Each object contains details like title, year, etc.
        """
        try:
            movies = self.ia.search_movie(movie_name)
            return movies
        except Exception as e:
            print(f"An error occurred while searching for movies: {e}")
            return []

    def get_imdb_id(self, movie_name):
        """
        Retrieves the IMDb ID of the first matching movie from the search results.

        Args:
            movie_name (str): The name of the movie to search for.

        Returns:
            str: The IMDb ID of the movie, or None if no match is found.
        """
        movies = self.search_movie(movie_name)
        if movies:
            return movies[0].movieID
        return None

    def get_movie_details(self, imdb_id):
        """
        Retrieves detailed information about a movie using its IMDb ID.

        Args:
            imdb_id (str): The IMDb ID of the movie.

        Returns:
            dict: A dictionary containing detailed information about the movie,
                  such as title, year, rating, genres, cast, and director.
        """
        try:
            movie = self.ia.get_movie(imdb_id)
            return movie
        except Exception as e:
            print(f"An error occurred while fetching movie details: {e}")
            return {}

    def get_movie_title(self, imdb_id):
        """
        Retrieves the title of a movie using its IMDb ID.

        Args:
            imdb_id (str): The IMDb ID of the movie.

        Returns:
            str: The title of the movie, or None if not available.
        """
        movie = self.get_movie_details(imdb_id)
        return movie.get("title")

    def get_movie_rating(self, imdb_id):
        """
        Retrieves the IMDb rating of a movie using its IMDb ID.

        Args:
            imdb_id (str): The IMDb ID of the movie.

        Returns:
            float: The IMDb rating of the movie, or None if not available.
        """
        movie = self.get_movie_details(imdb_id)
        return movie.get("rating")

    def get_movie_cast(self, imdb_id, max_cast=5):
        """
        Retrieves the top cast members of a movie using its IMDb ID.

        Args:
            imdb_id (str): The IMDb ID of the movie.
            max_cast (int): The maximum number of cast members to return. Defaults to 5.

        Returns:
            list: A list of top cast members, or an empty list if not available.
        """
        movie = self.get_movie_details(imdb_id)
        cast = movie.get("cast", [])
        return cast[:max_cast]

    def get_movie_director(self, imdb_id):
        """
        Retrieves the director(s) of a movie using its IMDb ID.

        Args:
            imdb_id (str): The IMDb ID of the movie.

        Returns:
            list: A list of directors, or an empty list if not available.
        """
        movie = self.get_movie_details(imdb_id)
        return movie.get("director", [])

    def get_movie_genres(self, imdb_id):
        """
        Retrieves the genres of a movie using its IMDb ID.

        Args:
            imdb_id (str): The IMDb ID of the movie.

        Returns:
            list: A list of genres, or an empty list if not available.
        """
        movie = self.get_movie_details(imdb_id)
        return movie.get("genres", [])
