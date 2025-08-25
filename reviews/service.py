from reviews.repository import ReviewsRepository


class ReviewsService:
    def __init__(self):
        self.__repository = ReviewsRepository()
    
    def get_reviews(self):
        return self.__repository.get_reviews()
    
    def create_review(self, stars, comment, movie):
        review = dict(
            stars=stars,
            comment=comment,
            movie=movie
        )
        return self.__repository.create_reviews(review)
