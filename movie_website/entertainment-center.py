import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 
	"a story of a boy ... ", 
	"http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg", 
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

titanic = media.Movie("Titanic", 
	"In 1996, treasure hunter Brock Lovett ... ", 
	"https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg", 
	"https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

movies = [toy_story, titanic]
# fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
