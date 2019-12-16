import csv


class MovieManager:
    movies = {}
    genres = {}

    def __init__(self, filename):
        with open(filename, "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.movies[row[0]] = row

        with open("data/genres.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.genres[row[0]] = row[1]

    def getGenres(self):
        return self.genres

    def getMovies(self):
        return self.movies

    def getNameFromID(self, movieID):
        return self.movies[movieID][1]

    def getRatingFromID(self, movieID):
        return self.movies[movieID][2]

    def getGenresFromID(self, movieID):
        return [self.getGenreFromGenreID(x) for x in self.movies[movieID][3].split(";")]

    def getGenreFromGenreID(self, genreID):
        return self.genres[genreID]

    def sort(self, userGenreRatings):
        ratings = []

        for i in self.movies:
            ratings.append(
                [int(self.getRatingFromID(i[0])) * sum([userGenreRatings[x] for x in self.getGenresFromID(i[0])]),
                 i[0]])

        bubbleSort(ratings)

        return ratings

    def unload(self):
        self.movies.clear()
        self.genres.clear()

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