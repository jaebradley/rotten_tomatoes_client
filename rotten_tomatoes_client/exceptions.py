class RottenTomatoesClientException(Exception):
    pass


class InvalidSearchParameters(RottenTomatoesClientException):
    pass


class InvalidMovieBrowsingParameters(RottenTomatoesClientException):
    pass


class InvalidTvShowBrowsingParameters(RottenTomatoesClientException):
    pass


class InvalidMovieDetailsParameters(RottenTomatoesClientException):
    pass


class RottenTomatoesServiceIsUnavailable(RottenTomatoesClientException):
    pass


class UnableToConnectToRottenTomatoesService(RottenTomatoesClientException):
    pass
