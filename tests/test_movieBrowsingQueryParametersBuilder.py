from unittest import TestCase
from mock import patch

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
    minimum_rating_value = "minimum rating"
    maximum_rating_value = "maximum rating"
    certified_fresh_value = "certified fresh"
    sort_by_value = "sort by"
    category_value = "category"
    base_expected = {
        "minTomato": minimum_rating_value,
        "maxTomato": maximum_rating_value,
        "certified": certified_fresh_value,
        "sort": sort_by_value,
        "type": category_value
    }

    def test_concatenated_values(self):
        values = ["1", "2", "3"]
        expected = "1;2;3"
        self.assertEqual(MovieBrowsingQueryParametersBuilder.get_concatenated_values(values=values), expected)

    def test_when_services_and_genres_are_not_defined(self):
        query = MockQuery(minimum_rating=self.minimum_rating_value, maximum_rating=self.maximum_rating_value,
                          services=None, certified_fresh=self.certified_fresh_value, genres=None,
                          sort_by=self.sort_by_value, category=self.category_value)

        self.assertEqual(MovieBrowsingQueryParametersBuilder.build(query=query), self.base_expected)

    def test_when_services_and_genres_are_empty(self):
        query = MockQuery(minimum_rating=self.minimum_rating_value, maximum_rating=self.maximum_rating_value,
                          services=[], certified_fresh=self.certified_fresh_value, genres=[],
                          sort_by=self.sort_by_value, category=self.category_value)

        self.assertEqual(MovieBrowsingQueryParametersBuilder.build(query=query), self.base_expected)

    @patch("rotten_tomatoes.query.parameters.builders.browsing.MovieBrowsingQueryParametersBuilder.get_concatenated_values")
    def test_when_services_are_defined(self, mock_concatenated_values):
        mock_concatenated_values.return_value = "mock concatenated values"
        query = MockQuery(minimum_rating=self.minimum_rating_value, maximum_rating=self.maximum_rating_value,
                          services=[1, 2, 3], certified_fresh=self.certified_fresh_value, genres=None,
                          sort_by=self.sort_by_value, category=self.category_value)

        expected_services = "mock concatenated values"
        expected = self.base_expected.copy()

        expected["services"] = expected_services

        self.assertEqual(MovieBrowsingQueryParametersBuilder.build(query=query), expected)

    @patch("rotten_tomatoes.query.parameters.builders.browsing.MovieBrowsingQueryParametersBuilder.get_concatenated_values")
    def test_when_genres_are_defined(self, mock_concatenated_values):
        mock_concatenated_values.return_value = "mock concatenated values"
        query = MockQuery(minimum_rating=self.minimum_rating_value, maximum_rating=self.maximum_rating_value,
                          services=None, certified_fresh=self.certified_fresh_value, genres=[1, 2, 3],
                          sort_by=self.sort_by_value, category=self.category_value)

        expected_services = "mock concatenated values"
        expected = self.base_expected.copy()

        expected["genres"] = expected_services

        self.assertEqual(MovieBrowsingQueryParametersBuilder.build(query=query), expected)
