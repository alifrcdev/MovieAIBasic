def getStringWithOptions(prompt, options, minLength=1):
    while True:
        string = input(prompt)
        if string not in options:
            print("Type only " + ", ".join(options) + ".")
        else:
            return string


userMovies = {}
genreRating = {}
movies = [
    [0, "Awakenings", 8, [0, 4]],
    [1, "A League of Their Own", 7, [0, 5, 6]],
    [2, "A Bronx Tale", 8, [0, 7, 8]],
    [3, "Angels in the Outfield", 6, [5, 6, 9]],
    [4, "A Time to Kill", 8, [0, 7, 10]],
    [5, "Amistad", 7, [0, 11]],
    [6, "Amistad 2", 5, [0, 7, 11]],
    [7, "Anaconda", 5, [1, 2, 12]]
]

genres = [
    "Drama",
    "Action",
    "Horror",
    "Sci-Fi",
    "Biography",
    "Comedy",
    "Family",
    "Crime",
    "Romance",
    "Fantasy",
    "Thriller",
    "History",
    "Adventure"
]

while True:

    for i in movies:
        if i[0] in userMovies:
            for genre in [genres[x] for x in movies[i[0]][3]]:
                rating = userMovies[i[0]][1] == "True"
                if genre in genreRating:
                    genreRating[genre] += rating
                else:
                    genreRating[genre] = rating

    for i in genres:
        if i not in genreRating:
            genreRating[i] = 0

    best = []
    best_index = 0
    best_rating = -10
    for i in range(len(movies)):
        if not i in userMovies:
            current_rating = movies[i][2] + pow(sum([genreRating[x] for x in [genres[x] for x in movies[i][3]]]), 2)
            if best_rating < current_rating:
                best_index = i
                best_rating = current_rating

    for i in range(len(movies)):
        if not i in userMovies:
            print(movies[i][1] + ": " + ", ".join([genres[x] for x in movies[i][3]]))

    if len(userMovies) == len(movies):
        print("Congrats! You have watched all our films.")
        exit(0)

    print(movies[best_index][1] + ": " + ", ".join([genres[x] for x in movies[best_index][3]]))

    liked = getStringWithOptions("Did you like the movie? (yes/no): ", ["yes", "no"])

    userMovies[movies[best_index][0]] = liked
