from libs import inputs
from libs import movieManager
from libs import table
from libs import userManager

username = inputs.getString("Enter your username: ")

movies = movieManager.MovieManager("data/movies.csv")
user = userManager.UserManager("users/" + username + ".csv")

for i in movies.getMovies():
    if user.didWatchMovie(i[0]):
        for genre in movies.getGenresFromID(i[0]):
            user.addGenreRating(genre,1 if user.isMovieLiked(i[0]) else 0)

user.fixGenres(movies)

data = []

for i in movies.sort(user.getGenreRatings()):
    if not user.didWatchMovie(i[1]):
        print(movies.getNameFromID(i[1]))
        data.append([i[1], movies.getNameFromID(i[1])])

table.printTable("Select Movie To Watch", ["Id", "Movie"], data)
movieNo = inputs.getSafeInt("Enter movie no: ")

liked = inputs.getSafeStrBool("Did you like the movie? (True/False)")
