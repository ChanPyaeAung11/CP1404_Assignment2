"""
Name: Chan Pyae Aung
Date Started: 5 Jan 2020
GitHub URL: https://github.com/JCUS-CP1404/assignment-02-ChanPyaeAung11
"""


class Movie:

    def __init__(self, title="", year=0, category="", is_watched=False):
        """ use parameters passed in this and construct them"""
        self.title = title
        self.year = year
        self.category = category
        self.is_watched = is_watched

    def __str__(self):
        """ return strings about movie details"""
        return f"{self.title},{self.year},{self.category},{self.is_watched}"

    def check_unwatched(self):
        """ return False if a movie is unwatched"""
        self.is_watched = False

    def check_watched(self):
        """ return True if a movie is watched"""
        self.is_watched = True

    def year_level(self):
        return int(self.year) <= 10000

    def save_movie(self):
        """ formatting the movie data to be put into csv"""
        watched = 'w' if self.is_watched else 'u'
        return f"{self.title},{self.year},{self.category},{watched} \n"
