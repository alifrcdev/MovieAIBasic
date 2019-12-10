import csv
import io

class UserManager:
    userMovies = {}
    genreRating = {}

    file = ""

    def __init__(self, filename):
        try:
            self.file = open(filename, "r+")
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
            return self.userMovies[movieID][1] == "True"
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

    def watched(self, movieId, liked):
        self.file.seek(0, io.SEEK_END)
        self.file.write(str(movieId) + "," + ("True" if liked == "yes" else "False") + "\n")

    def unload(self):
        self.file.close()
        self.genreRating.clear()
        self.userMovies.clear()
