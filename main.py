from libs import inputs

def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j][0] < arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


userMovies = {}
genreRating = {}
movies = [
    [0, "Awakenings", 8, [0, 4]],
    [1, "A League of Their Own", 7, [0, 5, 6]],
    [2, "A Bronx Tale", 8, [0, 7, 8]],
    [3, "Angels in the Outfield", "6", [5, 6, 9]],
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

    data = []
    ratings = []

    for i in movies:
        ratings.append([movies[i[0]][2] * sum([genreRating[x] for x in [genres[x] for x in movies[i[0]][3]]]), i[0]])

    bubbleSort(ratings)
    for i in ratings:
        if not i[1] in userMovies:
            data.append([i[1], movies[i[1]][1], ", ".join([genres[x] for x in movies[i[0]][3]])])

    if len(data) == 0:
        print("Congrats! You have watched all our films.")
        exit(0)

    print(data[0][1] + ": " + data[0][2])

    liked = inputs.getStringWithOptions("Did you like the movie? (yes/no): ", ["yes", "no"])

    userMovies[data[0][0]] = liked


