# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser

class Movie():
    """ This class provides a way to store movie related information"""

    def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_youtube_url, release_year):
        """Initialize instance of class Movie

        Args:
            movie_title: Title of movie for instance of class
            movie_storyline: Brief summary of plot
            poster_image_url: location for image, refcatored to be local
            trailer_youtube_url: url for the movie's official trailer
            release_year: year of the movie's release in the United States
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.release_year = release_year

    def show_trailer(self):
        """Opens movie's youtube trailer in web browser"""
        webbrowser.open(self.trailer_youtube_url)
