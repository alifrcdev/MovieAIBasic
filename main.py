from libs import helpers
from libs import inputs
from libs import movieManager
from libs import table
from libs import userManager

username = inputs.getString("Enter your username: ")

movies = movieManager.MovieManager("data/movies.csv")

while True:
    user = userManager.UserManager("users/" + username + ".csv")

    for i in movies.getMovies():
        if user.didWatchMovie(i[0]):
            for genre in movies.getGenresFromID(i[0]):
                user.addGenreRating(genre, 2 if user.isMovieLiked(i[0]) else -1)

    user.fixGenres(movies)

    data = []

    for i in movies.sort(user.getGenreRatings()):
        if not user.didWatchMovie(i[1]):
            print(movies.getNameFromID(i[1]))
            data.append([i[1], movies.getNameFromID(i[1]), ", ".join(movies.getGenresFromID(i[1]))])

    if len(data) == 0:
        print("Congrats! You have watched all our films.")
        user.unload()
        movies.unload()
        data.clear()
        exit(0)

    table.printTable("Select Movie To Watch", ["Movie", "Genres"], helpers.columnsAfter(data, 1))
    movieNo = inputs.getSafeIntWithRange("Enter movie no: ", 1, len(data))

    liked = inputs.getStringWithOptions("Did you like the movie? (yes/no): ", ["yes", "no"])

    user.watched(data[movieNo - 1][0], liked)

    user.unload()
