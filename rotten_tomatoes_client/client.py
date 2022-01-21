import requests

from rotten_tomatoes_client.exceptions import InvalidSearchParameters, RottenTomatoesServiceIsUnavailable, \
    UnableToConnectToRottenTomatoesService, InvalidMovieBrowsingParameters, InvalidTvShowBrowsingParameters, \
    InvalidMovieDetailsParameters
from rotten_tomatoes_client.query.parameters.browsing import TvBrowsingCategory
from rotten_tomatoes_client.query.parameters.builders.browsing import MovieBrowsingQueryParametersBuilder


class RottenTomatoesClient:
    BASE_URL = "https://www.rottentomatoes.com/api/private"
    BASE_V1_URL = "{base_url}/v1.0".format(base_url=BASE_URL)
    BASE_V2_URL = "{base_url}/v2.0".format(base_url=BASE_URL)
    MOVIE_DETAILS_URL = "{base_url}/movies".format(base_url=BASE_V1_URL)
    SEARCH_URL = "{base_url}/search".format(base_url=BASE_V2_URL)
    BROWSE_URL = "{base_url}/browse".format(base_url=BASE_V2_URL)

    def __init__(self):
        pass

    @staticmethod
    def search(term, limit=10):
        return RottenTomatoesClient.handle_response(
            response=requests.get(url=RottenTomatoesClient.SEARCH_URL, params={"q": term, "limit": limit}),
            invalid_request_error=InvalidSearchParameters
        )

    @staticmethod
    def browse_movies(query):
        return RottenTomatoesClient.handle_response(
            response=requests.get(url=RottenTomatoesClient.BROWSE_URL,
                                  params=MovieBrowsingQueryParametersBuilder.build(query=query)),
            invalid_request_error=InvalidMovieBrowsingParameters
        )

    @staticmethod
    def browse_tv_shows(category=TvBrowsingCategory.most_popular):
        return RottenTomatoesClient.handle_response(
            response=requests.get(url=RottenTomatoesClient.BROWSE_URL, params={"type": category.value}),
            invalid_request_error=InvalidTvShowBrowsingParameters
        )

    @staticmethod
    def get_movie_details(movie_id):
        return RottenTomatoesClient.handle_response(
            response=requests.get(url="{movie_details_url}/{movie_id}"
                                  .format(movie_details_url=RottenTomatoesClient.MOVIE_DETAILS_URL, movie_id=movie_id)),
            invalid_request_error=InvalidMovieDetailsParameters
        )

    @staticmethod
    def handle_response(response, invalid_request_error):
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_error:
            if 400 <= http_error.response.status_code < 500:
                raise invalid_request_error()
            elif 500 <= http_error.response.status_code < 600:
                raise RottenTomatoesServiceIsUnavailable()
            else:
                raise http_error
        except requests.exceptions.ConnectTimeout:
            raise UnableToConnectToRottenTomatoesService()

        return response.json()
