import csv
from . import helpers

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
        ratings = {}

        a = 0
        for i in self.movies:
            ratings[a] = [int(self.getRatingFromID(i[0])) + sum([userGenreRatings[x] for x in self.getGenresFromID(i[0])]), i[0]]
            a=a+1

        helpers.bubbleSort(ratings)

        return ratings
