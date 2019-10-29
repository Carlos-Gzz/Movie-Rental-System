from MovieApp import Movie

class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {}>".format(self.name)

    def add_movie(self, name, genre):
        movie = Movie(name, genre, False)
        self.movies.append(movie)

    def delete_movie(self, name):
        self.movies = list(filter(lambda y: y.name != name, self.movies))

    def watched_movies(self):
        watched_movies = list(filter(lambda x: x.watched, self.movies))
        return watched_movies

    def set_watched(self, name):
        for movie in self.movies:
            if movie.name == name:
                movie.watched = True

    def json(self):
        return{
            "name": self.name,
            #"movies": self.movies. in this case, a 'for' was used for name, genre, watched.
            "movies": [
                movie.json() for movie in self.movies
            ]

        }
    @classmethod
    def from_json(cls, json_data):
        user = User(json_data['name'])
        movies = []
        for movie_data in json_data["movies"]:
            movies.append(Movie.from_json(movie_data))
        user.movies = movies

        return user