import requests

from rotten_tomatoes_client.query.parameters.builders.browsing import MovieBrowsingQueryParametersBuilder
from rotten_tomatoes_client.query.parameters.browsing import TvBrowsingCategory


class RottenTomatoesClient:
    BASE_URL = "https://www.rottentomatoes.com/api/private/v2.0"
    SEARCH_URL = "{base_url}/search".format(base_url=BASE_URL)
    BROWSE_URL = "{base_url}/browse".format(base_url=BASE_URL)

    def __init__(self):
        pass

    @staticmethod
    def search(term):
        r = requests.get(url=RottenTomatoesClient.SEARCH_URL, params={"q": term})

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
