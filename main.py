from libs import inputs
from libs import movieManager
from libs import userManager

username = inputs.getString("Enter your username: ")

movies = movieManager.MovieManager("data/movies.csv")
user = userManager.UserManager("users/" + username + ".csv")

for i in movies.getMovies():
    if user.didWatchMovie(i[0]):
        for genre in movies.getGenresFromID(i[0]):
            user.addGenreRating(genre,1 if user.isMovieLiked(i[0]) else 0)

user.fixGenres(movies)

for i in movies.sort(user.getGenreRatings()):
    if not user.didWatchMovie(i[1]):
        print(movies.getNameFromID(i[1]))
