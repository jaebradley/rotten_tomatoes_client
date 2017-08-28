from unittest import TestCase
from mock import patch

from rotten_tomatoes_client.query.parameters.builders.browsing import MovieBrowsingQueryParametersBuilder


class MockQuery:
    def __init__(self, minimum_rating, maximum_rating, services, certified_fresh,
                 genres, sort_by, category, page, limit):
        self.minimum_rating = minimum_rating
        self.maximum_rating = maximum_rating
        self.services = services
        self.certified_fresh = certified_fresh
        self.genres = genres
        self.sort_by = sort_by
        self.category = category
        self.page = page
        self.limit = limit


class MockValue:
    def __init__(self, value):
        self.value = value


class TestMovieBrowsingQueryParametersBuilder(TestCase):
    minimum_rating_value = "minimum rating"
    maximum_rating_value = "maximum rating"
    certified_fresh_value = "certified fresh"
    sort_by_value = MockValue(value="sort by")
    category_value = MockValue(value="category")
    page = "page"
    limit = "limit"
    base_expected = {
        "minTomato": minimum_rating_value,
        "maxTomato": maximum_rating_value,
        "certified": certified_fresh_value,
        "sort": "sort by",
        "type": "category",
        "page": page,
        "limit": limit
    }
    value_1 = MockValue(value="1")
    value_2 = MockValue(value="2")
    value_3 = MockValue(value="3")
    values = [value_1, value_2, value_3]

    def test_concatenated_values(self):
        expected = "1;2;3"
        self.assertEqual(MovieBrowsingQueryParametersBuilder.get_concatenated_values(values=self.values), expected)

    def test_when_services_and_genres_are_not_defined(self):
        query = MockQuery(minimum_rating=self.minimum_rating_value, maximum_rating=self.maximum_rating_value,
                          services=None, certified_fresh=self.certified_fresh_value, genres=None,
                          sort_by=self.sort_by_value, category=self.category_value, page=self.page, limit=self.limit)

        self.assertEqual(MovieBrowsingQueryParametersBuilder.build(query=query), self.base_expected)

    def test_when_services_and_genres_are_empty(self):
        query = MockQuery(minimum_rating=self.minimum_rating_value, maximum_rating=self.maximum_rating_value,
                          services=[], certified_fresh=self.certified_fresh_value, genres=[],
                          sort_by=self.sort_by_value, category=self.category_value, page=self.page, limit=self.limit)

        self.assertEqual(MovieBrowsingQueryParametersBuilder.build(query=query), self.base_expected)

    @patch("rotten_tomatoes_client.query.parameters.builders.browsing.MovieBrowsingQueryParametersBuilder.get_concatenated_values")
    def test_when_services_are_defined(self, mock_concatenated_values):
        mock_concatenated_values.return_value = "mock concatenated values"
        query = MockQuery(minimum_rating=self.minimum_rating_value, maximum_rating=self.maximum_rating_value,
                          services=self.values, certified_fresh=self.certified_fresh_value, genres=None,
                          sort_by=self.sort_by_value, category=self.category_value, page=self.page, limit=self.limit)

        expected_services = "mock concatenated values"
        expected = self.base_expected.copy()

        expected["services"] = expected_services

        self.assertEqual(MovieBrowsingQueryParametersBuilder.build(query=query), expected)

    @patch("rotten_tomatoes_client.query.parameters.builders.browsing.MovieBrowsingQueryParametersBuilder.get_concatenated_values")
    def test_when_genres_are_defined(self, mock_concatenated_values):
        mock_concatenated_values.return_value = "mock concatenated values"

        query = MockQuery(minimum_rating=self.minimum_rating_value, maximum_rating=self.maximum_rating_value,
                          services=None, certified_fresh=self.certified_fresh_value, genres=self.values,
                          sort_by=self.sort_by_value, category=self.category_value, page=self.page, limit=self.limit)

        expected_services = "mock concatenated values"
        expected = self.base_expected.copy()

        expected["genres"] = expected_services

        self.assertEqual(MovieBrowsingQueryParametersBuilder.build(query=query), expected)
