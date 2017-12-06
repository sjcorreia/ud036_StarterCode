from __future__ import print_function
import media
import fresh_tomatoes
import json


def main():
    """Create the content for the 'Fresh Tomatoes Movie Trailers'
    Website.

    This function will read from a JSON file containing some 
    of my favortie movies and create a list of media.Movie 
    objects to pass to the fresh_tomatoes.open_movies_page()
    function. 

    """

    movies_list = []
    
    with open('json/movies.json') as json_data_movies:
        # JSON file format is a common, the idea is to mimic reading
        # from a simplified and simulated database.
        # Reading from a JSON file into a python dict, or list of dicts
        data_movies = json.load(json_data_movies)
    
        for movie in data_movies["favoriteMovies"]:
            movies_list.append(media.Movie(movie["movieTitle"],
                                           movie["posterLink"],
                                           movie["trailerLink"],
                                           movie["yearReleased"]))
    
    # create HTML site via fresh_tomatoes module
    fresh_tomatoes.open_movies_page(movies_list)


if __name__ == "__main__":
    main()