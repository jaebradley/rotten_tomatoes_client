from unittest import TestCase

from rotten_tomatoes.client import RottenTomatoesClient
from rotten_tomatoes.query import MovieBrowsingQuery


class RottenTomatoesClientIntegrationTest(TestCase):
    def test_search(self):
        result = RottenTomatoesClient.search(term="Godfather")
        self.assertIsNotNone(result)
        self.assertTrue("actorCount" in result)
        self.assertTrue("actors" in result)
        self.assertTrue("criticCount" in result)
        self.assertTrue("critics" in result)
        self.assertTrue("franchiseCount" in result)
        self.assertTrue("franchises" in result)
        self.assertTrue("movieCount" in result)
        self.assertTrue("movies" in result)
        self.assertTrue("tvCount" in result)
        self.assertTrue("tvSeries" in result)

    def test_browse_tv_shows(self):
        result = RottenTomatoesClient.browse_tv_shows()
        self.assertIsNotNone(result)
        self.assertTrue("counts" in result)
        self.assertTrue("results" in result)


    def test_browse_movies(self):
        result = RottenTomatoesClient.browse_movies(query=MovieBrowsingQuery())
        self.assertIsNotNone(result)
        self.assertTrue("counts" in result)
        self.assertTrue("results" in result)