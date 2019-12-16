from libs import inputs
from libs import movieManager

userMovies = {}
genreRating = {}

movies = movieManager.MovieManager("data/movies.csv")

while True:

    for i in movies.getMovies():
        if i[0] in userMovies:
            for genre in movies.getGenresFromID(i[0]):
                rating = userMovies[i[0]][1] == "True"
                if genre in genreRating:
                    genreRating[genre] += rating
                else:
                    genreRating[genre] = rating

    for i in movies.getGenres():
        i = movies.getGenreFromGenreID(i)
        if not i in genreRating:
            genreRating[i] = 0

    data = []

    for i in movies.sort(genreRating):
        if not i[1] in userMovies:
            data.append([i[1], movies.getNameFromID(i[1]), ", ".join(movies.getGenresFromID(i[1]))])

    if len(data) == 0:
        print("Congrats! You have watched all our films.")
        movies.unload()
        data.clear()
        exit(0)

    print(data[0][1] + ": " + data[0][2])

    liked = inputs.getStringWithOptions("Did you like the movie? (yes/no): ", ["yes", "no"])

    userMovies[data[0][0]] = liked
