from genres.repository import GenreRepository


class GenreService:

    def __init__(self):
        self.__repository = GenreRepository()

    def get_genres(self):
        return self.__repository.get_genres()

    def create_genre(self, name):
        genre = dict(
            name=name,
        )
        return self.__repository.create_genres(genre)