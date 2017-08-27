import requests

from rotten_tomatoes_client.query.parameters.builders.browsing import MovieBrowsingQueryParametersBuilder
from rotten_tomatoes_client.query.parameters.browsing import TvBrowsingCategory


class RottenTomatoesClient:
    BASE_URL = "https://www.rottentomatoes.com/api/private"
    BASE_V1_URL = "{base_url}/v1.0".format(base_url=BASE_URL)
    BASE_V2_URL = "{base_url}/v2.0".format(base_url=BASE_URL)
    MOVIE_DETAILS_URL = "{base_url}/v1.0/movies".format(base_url=BASE_V1_URL)
    SEARCH_URL = "{base_url}/search".format(base_url=BASE_V2_URL)
    BROWSE_URL = "{base_url}/browse".format(base_url=BASE_V2_URL)

    def __init__(self):
        pass

    @staticmethod
    def search(term, limit=10):
        r = requests.get(url=RottenTomatoesClient.SEARCH_URL, params={"q": term, "limit": limit})

        r.raise_for_status()

        return r.json()

    @staticmethod
    def browse_movies(query):
        parameters = MovieBrowsingQueryParametersBuilder.build(query=query)

        r = requests.get(url=RottenTomatoesClient.BROWSE_URL, params=parameters)

        r.raise_for_status()

        return r.json()

    @staticmethod
    def browse_tv_shows(category=TvBrowsingCategory.most_popular):
        r = requests.get(url=RottenTomatoesClient.BROWSE_URL, params={"type": category.value})

        r.raise_for_status()

        return r.json()

    @staticmethod
    def get_movie_details(movie_id):
        r = requests.get(url="{movie_details_url}/{movie_id}"
                         .format(movie_details_url=RottenTomatoesClient.MOVIE_DETAILS_URL, movie_id=movie_id))

        r.raise_for_status()

        return r.json()

