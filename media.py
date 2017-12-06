from __future__ import print_function

class Movie():
    """This class provides a simple way to store movie related 
    information
    
    Attributes:
    title: a string for the title of the movie
    poster_image_url: a string containing a url for the movie poster
    trailer_youtube_url: a string containing the url of the youtube trailer
    """

    def __init__(self, movie_title, poster_image, trailer_youtube,
                 year_released):
        # class constructor
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = year_released
