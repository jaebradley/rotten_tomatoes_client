from enum import Enum


class TvBrowsingCategory(Enum):
    new_tv_tonight = "tv-list-1"
    most_popular = "tv-list-2"
    certified_fresh = "tv-list-3"


class Service(Enum):
    amazon = "amazon"
    hbo_go = "hbo_go"
    itunes = "itunes"
    netflix = "netflix_iw"
    vudu = "vudu"
    amazon_prime = "amazon_prime"
    fandango_now = "fandango_now"


class SortBy(Enum):
    release = "release"
    popularity = "popularity"


class MovieBrowsingCategory(Enum):
    opening_in_theaters = "opening"
    in_theaters = "in-theaters"
    upcoming_in_theaters = "upcoming"
    certified_fresh_in_theaters = "cf-in-theaters"
    all_dvd_and_streaming = "dvd-streaming-all"
    top_dvd_and_streaming = "top-dvd-streaming"
    new_dvd_and_streaming = "dvd-streaming-new"
    upcoming_dvd_and_streaming = "dvd-streaming-upcoming"
    certified_fresh_dvd_and_streaming = "cf-dvd-streaming-all"


class Genre(Enum):
    action = 1
    animation = 2
    art_and_foreign = 3
    classics = 4
    comedy = 5
    documentary = 6
    drama = 7
    horror = 8
    kids_and_family = 9
    mystery = 10
    romance = 11
    sci_fi_and_fantasy = 12
