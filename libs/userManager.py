import csv


class UserManager:
    userMovies = {}
    genreRating = {}

    file = ""

    def __init__(self, filename):
        try:
            self.file = open(filename)
            csv_reader = csv.reader(self.file, delimiter=',')
            for row in csv_reader:
                self.userMovies[row[0]] = row[1]

        except FileNotFoundError:
            self.file = open(filename, "w+")
            print("Creating new profile.")



    def didWatchMovie(self,movieID):
        if movieID in self.userMovies:
            return True
        else:
            return False

    def isMovieLiked(self, movieID):
        if movieID in self.userMovies:
            return self.userMovies[movieID]
        else:
            return None

    def getMovies(self):
        return self.userMovies

    def addGenreRating(self, genreID, rating):
        if genreID in self.genreRating:
            self.genreRating[genreID] += rating
        else:
            self.genreRating[genreID] = rating

    def getGenreRatings(self):
        return self.genreRating

    def fixGenres(self, movieManager):
        for i in movieManager.getGenres():
            i = movieManager.getGenreFromGenreID(i)
            if not i in self.genreRating:
                self.genreRating[i] = 0