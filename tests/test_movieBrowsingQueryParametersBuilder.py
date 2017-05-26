from unittest import TestCase

from rotten_tomatoes.query.parameters.builders.browsing import MovieBrowsingQueryParametersBuilder


class MockQuery:
    def __init__(self, minimum_rating, maximum_rating, services, certified_fresh,
                 genres, sort_by, category):
        self.minimum_rating = minimum_rating
        self.maximum_rating = maximum_rating
        self.services = services
        self.certified_fresh = certified_fresh
        self.genres = genres
        self.sort_by = sort_by
        self.category = category


class TestMovieBrowsingQueryParametersBuilder(TestCase):
    def test_when_no_services_or_genres_are_defined(self):
        minimum_rating_value = "minimum rating"
        maximum_rating_value = "maximum rating"
        certified_fresh_value = "certified fresh"
        sort_by_value = "sort by"
        category_value = "category"
        query = MockQuery(minimum_rating=minimum_rating_value, maximum_rating=maximum_rating_value, services=None,
                          certified_fresh=certified_fresh_value, genres=None, sort_by=sort_by_value, category=category_value)

        expected = {
            "minTomato": minimum_rating_value,
            "maxTomato": maximum_rating_value,
            "certified": certified_fresh_value,
            "sort": sort_by_value,
            "type": category_value
        }

        self.assertEqual(MovieBrowsingQueryParametersBuilder.build(query=query), expected)
