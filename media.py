import webbrowser

class Movie():
    """ This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

        #Figure out if rating is valid
	if movie_rating in self.VALID_RATINGS:
	    self.movie_rating = movie_rating
	else:
	    self.movie_rating = "Unknown"
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
        
