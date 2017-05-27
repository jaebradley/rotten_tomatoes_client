from rotten_tomatoes_client.query.parameters.browsing import SortBy, MovieBrowsingCategory


class MovieBrowsingQuery:
    def __init__(self, minimum_rating=70, maximum_rating=100, services=None, certified_fresh=False,
                 genres=None, sort_by=SortBy.popularity, category=MovieBrowsingCategory.opening_in_theaters):
        self.minimum_rating = minimum_rating
        self.maximum_rating = maximum_rating
        self.services = services
        self.certified_fresh = certified_fresh
        self.genres = genres
        self.sort_by = sort_by
        self.category = category
