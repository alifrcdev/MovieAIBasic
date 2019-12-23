def input_opts(prompt, options):
    while True:
        string = input(prompt).lower()
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
    [7, "Hababam Sınıfı 1", 5, [5, 6]],
    [8, "Hababam Sınıfı 2", 8, [5, 6]],
    [9, "Hababam Sınıfı 3", 3, [5, 6]],
    [10, "Hababam Sınıfı 4", 6, [5, 6]],
    [11, "Hababam Sınıfı 5", 2, [5, 6]],
    [12, "Hababam Sınıfı 6", 7, [5, 6]],
    [13, "Hababam Sınıfı 7", 9, [5, 6]],
    [14, "Hababam Sınıfı 8", 1, [5, 6]]
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

    for i in range(len(genres)):
        genreRating[i] = 0

    for i in range(len(movies)):
        if i in userMovies:
            for genre in movies[i][3]:
                rating = 2
                if userMovies[i] == "no":
                    rating = -1
                if genre in genreRating:
                    genreRating[genre] += rating
                else:
                    genreRating[genre] = rating

    best = []
    best_index = None
    best_rating = -5.0
    for i in range(len(movies)):
        if i not in userMovies:
            current_rating = movies[i][2] + pow(sum([genreRating[x] for x in movies[i][3]]), 1)
            if best_rating < current_rating:
                best_index = i
                best_rating = current_rating

    if best_index is None:
        print("Congrats! You have watched all our films.")
        exit(0)

    print(movies[best_index][1] + ": " + ", ".join([genres[x] for x in movies[best_index][3]]))

    liked = input_opts("Did you like the movie? (yes/no): ", ["yes", "no"])

    userMovies[best_index] = liked

    genreRating.clear()
