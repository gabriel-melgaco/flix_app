from movies.repository import MovieRepository


class MovieService:
    def __init__(self):
        self.__repository = MovieRepository()

    def get_movies(self):
        return self.__repository.get_movies()
    
    def create_movie(self, title, release_date, resume, genre, actors):
        movie = dict(
            title=title,
            release_date=release_date,
            resume=resume,
            genre= genre,
            actors= actors,
        )
        return self.__repository.create_movie(movie)
    
    def get_movies_stats(self):
        return self.__repository.get_movies_stats()