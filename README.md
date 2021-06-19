[![Build Status](https://travis-ci.com/Genza999/rotten_tomatoes_client.svg?branch=update_readme)](https://travis-ci.com/Genza999/rotten_tomatoes_client)
[![PyPI version](https://badge.fury.io/py/rotten_tomatoes_client.svg)](https://badge.fury.io/py/rotten_tomatoes_client)

# Rotten Tomatoes Client (No API Key Necessary!)

* [Introduction](https://github.com/jaebradley/rotten_tomatoes_client/blob/master/README.md#introduction)
* [The Not-So-Private Public API](https://github.com/jaebradley/rotten_tomatoes_client/blob/master/README.md#the-not-so-private-public-api)
* [Client](https://github.com/jaebradley/rotten_tomatoes_client/blob/master/README.md#client)
  * [Installation](https://github.com/jaebradley/rotten_tomatoes_client/blob/master/README.md#installation)
  * [Search](https://github.com/jaebradley/rotten_tomatoes_client/blob/master/README.md#search)
  * [Browse TV Shows](https://github.com/jaebradley/rotten_tomatoes_client/blob/master/README.md#browse-tv-shows)
  * [Browse Movies](https://github.com/jaebradley/rotten_tomatoes_client/blob/master/README.md#browse-movies)


## Introduction

I think Rotten Tomatoes is a pretty neat service. So I wanted to try and work on a couple projects (like a command line tool) that incorporate data from Rotten Tomatoes.

After a short cursory investigation of existing Rotten Tomatoes Python clients (like [rottentomatoes](https://github.com/zachwill/rottentomatoes) and [rtsimple](https://github.com/celiao/rtsimple)) I noticed two things:

1. Each client requires an API key for use (which is reasonable)
2. The Rotten Tomatoes API is pretty hard to get access to (less reasonable).

For example:

> Rotten Tomatoes is no longer issuing API keys at the time of registration. We will review each application to ensure the usage of our data aligns with Brand Guidelines and Terms of Service and will provision keys if approved. There is now a license fee to access the API details of which will be provided upon application approval. The approval process may take up to 60 days. Thank you for your patience.

[From this GitHub issue](https://github.com/realpython/support/issues/268#issue-110173728).

> Thank you for your interest in the Rotten Tomatoes API. API users have access to our existing API, which provides full access to Rotten Tomatoes Scores and Reviews Snippets (up to 20), for an annual fee which starts at $60,000.

[From this Reddit thread](https://www.reddit.com/r/webdev/comments/4649rw/rotten_tomatoes_api/d03ap2u/?utm_content=permalink&utm_medium=front&utm_source=reddit&utm_name=webdev).

## The Not-So-Private Public API

If you go to, say, the ["Certified Fresh Movies" page](https://www.rottentomatoes.com/browse/cf-in-theaters?minPopcorn=0&maxPopcorn=100&genres=1;2;4;5;6;8;9;10;11;13;18;14&sortBy=popularity)

![alt-text](http://imgur.com/0LQf7NQ.png)

and open up the `Network` tab / development console in your browser, you can see HTTP `GET` requests like

```
https://www.rottentomatoes.com/api/private/v2.0/browse?minTomato=70&maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&certified=true&sortBy=popularity&type=cf-in-theaters
```

which returns a `JSON` response that looks like

```json
{
  "counts": {
    "count": 14,
    "total": 14
  },
  "debugUrl": "http://rt-client-facade-v2-6-1.aws.prod.flixster.com/list/top-box-office/movies?expand=true&include=%5B%22movieSupplementaryInfo%22%2C%22audienceSummary%22%2C%22affiliates%22%2C%22criticSummary%22%2C%22genres%22%2C%22moviePersonnel%22%2C%22moviePersonnel.actors%22%2C%22moviePersonnel.actors.person%22%5D&page=%7B%22limit%22%3A1000%7D",
  "results": [
    {
      "actors": [
        "Chris Pratt",
        "Zoe Saldana",
        "Dave Bautista"
      ],
      "id": 771385707,
      "mainTrailer": {
        "id": "11295755",
        "sourceId": "http://link.theplatform.com/s/NGweTC/media/dFLWRKu5WPrE"
      },
      "mpaaRating": "PG13",
      "popcornIcon": "upright",
      "popcornScore": 90,
      "posters": {
        "primary": "https://resizing.flixster.com/Qjh201ZZ1tydptY1QVjOJrYVAis=/130x0/v1.bTsxMjMyMzE1NjtwOzE3MzMyOzEyMDA7NTkxOzg3Ng",
        "thumborId": "v1.bTsxMjMyMzE1NjtwOzE3MzMyOzEyMDA7NTkxOzg3Ng"
      },
      "runtime": "2 hr. 17 min.",
      "synopsis": "<em>Guardians of the Galaxy Vol. 2</em>'s action-packed plot, dazzling visuals, and irreverent humor add up to a sequel that's almost as fun -- if not quite as thrillingly fresh -- as its predecessor.",
      "synopsisType": "consensus",
      "theaterReleaseDate": "May 5",
      "title": "Guardians of the Galaxy Vol. 2",
      "tomatoIcon": "certified_fresh",
      "tomatoScore": 81,
      "url": "/m/guardians_of_the_galaxy_vol_2"
    },
    {
      "actors": [
        "Michael Fassbender",
        "Katherine Waterston",
        "Billy Crudup"
      ],
      "id": 771377268,
      "mainTrailer": {
        "id": "11295756",
        "sourceId": "http://link.theplatform.com/s/NGweTC/media/fpqxfaxTIQdB"
      },
      "mpaaRating": "R",
      "popcornIcon": "upright",
      "popcornScore": 61,
      "posters": {
        "primary": "https://resizing.flixster.com/S2SZABT3ghBipL-urqBzBqhUs-E=/130x0/v1.bTsxMjM0NTY3NjtqOzE3MzMyOzEyMDA7NTM5OzgwMA",
        "thumborId": "v1.bTsxMjM0NTY3NjtqOzE3MzMyOzEyMDA7NTM5OzgwMA"
      },
      "runtime": "2 hr. 0 min.",
      "synopsis": "<em>Alien: Covenant</em> delivers another satisfying round of close-quarters deep-space terror, even if it doesn't take the saga in any new directions.",
      "synopsisType": "consensus",
      "theaterReleaseDate": "May 19",
      "title": "Alien: Covenant",
      "tomatoIcon": "certified_fresh",
      "tomatoScore": 71,
      "url": "/m/alien_covenant"
    },
    ...
  ]
}
```

Essentially, I've found these "public" endpoints for
1. Browsing Movies & TV Shows
    * Opening This Week, Top DVD & Streaming, New TV Tonight, etc.
2. Search
    * Keyword search for movies, franchises, actors, tv shows, etc.

I have *not* found endpoints for a given movie / tv show / actor, which is annoying.

## Client

Obviously, with a limited (known) API, there will be an equally limited client interface.
Additionally, it goes without saying that since this is not an officially-supported API, there are no guarantees about the reliability of this client.

### Installation

`pip install rotten_tomatoes_client`

### Search

The [`search` method](https://github.com/jaebradley/rotten_tomatoes_client/blob/master/rotten_tomatoes_client/client.py#L15-L21) takes a `term` to search for and a `limit`. The default `limit` value is `10`.

```python
from rotten_tomatoes_client import RottenTomatoesClient

result = RottenTomatoesClient.search(term="Indiana Jones", limit=5)

# The result will look something like this
# {
#     "actorCount": 0,
#     "actors": [],
#     "criticCount": 0,
#     "critics": [],
#     "franchiseCount": 1,
#     "franchises": [
#         {
#             "image": "https://resizing.flixster.com/s5UqfnC-acCiofUCK2UAyaNjADM=/fit-in/80x80/v1.bjsxNDMzNTI2O2o7MTczODY7MTIwMDs2MDA7MjYy",
#             "title": "Indiana Jones",
#             "url": "/franchise/indiana_jones"
#         }
#     ],
#     "movieCount": 31,
#     "movies": [
#         {
#             "castItems": [
#                 {
#                     "name": "Harrison Ford",
#                     "url": "/celebrity/harrison_ford"
#                 },
#                 {
#                     "name": "Karen Allen",
#                     "url": "/celebrity/karen_allen"
#                 },
#                 {
#                     "name": "Paul Freeman",
#                     "url": "/celebrity/1005456-paul_freeman"
#                 }
#             ],
#             "image": "https://resizing.flixster.com/AGuamVlV_ZyUguJynyXZz5eSapY=/fit-in/80x80/v1.bTsxMTE1NzYxNDtqOzE3NDA5OzEyMDA7MTAxMDsxNTAw",
#             "meterClass": "certified_fresh",
#             "meterScore": 94,
#             "name": "Raiders of the Lost Ark",
#             "subline": "Harrison Ford, Karen Allen, Paul Freeman, ",
#             "url": "/m/raiders_of_the_lost_ark",
#             "year": 1981
#         },
#         ...
#     ],
#     "tvCount": 0,
#     "tvSeries": []
# }
```

### Browse TV Shows

There are only three categories for browsing TV shows (located in the `TvBrowsingCategory` enum)
* `new_tv_tonight`
* `most_popular`
* `certified_fresh`

The [`browse_tv_shows` method](https://github.com/jaebradley/rotten_tomatoes_client/blob/master/rotten_tomatoes_client/client.py#L23-L31) takes [a `TvBrowsingCategory` value](https://github.com/jaebradley/rotten_tomatoes_client/blob/master/rotten_tomatoes_client/query/parameters/browsing.py#L4-L7). If none is provided, it defaults to using [`TvBrowsingCategory.most_popular`](https://github.com/jaebradley/rotten_tomatoes_client/blob/master/rotten_tomatoes_client/query/parameters/browsing.py#L6).

```python
from rotten_tomatoes_client import RottenTomatoesClient, TvBrowsingCategory

result = RottenTomatoesClient.browse_tv_shows(category=TvBrowsingCategory.most_popular)

# The result will look something like this
# {
#   "counts": {
#     "count": 16,
#     "total": 16
#   },
#   "results": [
#     {
#       "posters": {
#         "primary": "https://resizing.flixster.com/OcgpKual3yhynPR3ZbNl1NfHwUE=/2000x3000/v1.dDsyNTQ3OTI7ajsxNzMyNzsxMjAwOzIwMDA7MzAwMA"
#       },
#       "title": "Twin Peaks: The Return",
#       "tomatoIcon": "certified",
#       "tomatoScore": 95,
#       "url": "/tv/twin_peaks/s03"
#     },
#     {
#       "posters": {
#         "primary": "https://resizing.flixster.com/ON_GjiBNjJ8InbhnRnr0wCNKGAQ=/2048x3072/v1.dDsyNTI5MDY7ajsxNzMyNzsxMjAwOzIwNDg7MzA3Mg"
#       },
#       "title": "American Gods: Season 1",
#       "tomatoIcon": "certified",
#       "tomatoScore": 96,
#       "url": "/tv/american_gods/s01"
#     },
#     ...
#   ],
#   "title": "Most Popular TV on RT"
# }
```

### Browse Movies

The [`browse_movies` method](https://github.com/jaebradley/rotten_tomatoes_client/blob/master/rotten_tomatoes_client/client.py#L23-L31) takes [a `MovieBrowsingQuery`](https://github.com/jaebradley/rotten_tomatoes_client/blob/master/rotten_tomatoes_client/client.py#L23-L31) that is composed of the following parameters
* `minimum_rating`
  * Minimum allowable RottenTomatoes score
  * Defaults to `70`
* `maximum_rating`
  * Maximum allowable RottenTomatoes score
  * Defaults to `100`
* `services`
  * A `list` of any of [the `Service` enum values](https://github.com/jaebradley/rotten_tomatoes_client/blob/master/rotten_tomatoes_client/query/parameters/browsing.py#L10-L17) like [`Service.amazon`](https://github.com/jaebradley/rotten_tomatoes_client/blob/master/rotten_tomatoes_client/query/parameters/browsing.py#L11) or [`Service.netflix`](https://github.com/jaebradley/rotten_tomatoes_client/blob/master/rotten_tomatoes_client/query/parameters/browsing.py#L14).
  * Defaults to all streaming options.
* `certified_fresh`
  * A `boolean` that represents whether movies that are (or are not) "Certified Fresh" should be considered.
  * Defaults to `False`
* `genres`
  * A `list` of any of [the `Genre` enum values](https://github.com/jaebradley/rotten_tomatoes_client/blob/master/rotten_tomatoes_client/query/parameters/browsing.py#L37-L49) like [`Genre.action`](https://github.com/jaebradley/rotten_tomatoes_client/blob/master/rotten_tomatoes_client/query/parameters/browsing.py#L38) or [`Genre.comedy`](https://github.com/jaebradley/rotten_tomatoes_client/blob/master/rotten_tomatoes_client/query/parameters/browsing.py#L42).
  * Defaults to all genres.
* `sort_by`
  * Can either sort by popularity or release date using [the `SortBy` enum](https://github.com/jaebradley/rotten_tomatoes_client/blob/master/rotten_tomatoes_client/query/parameters/browsing.py#L20-L22).
  * Defaults to sorting by popularity
* `category`
  * Represents what types of movies to filter by, for example, ones that are opening in theaters, or have recently been released on DVD / streaming.
  * Takes any of [the `MovieBrowsingCategory` enum values](https://github.com/jaebradley/rotten_tomatoes_client/blob/master/rotten_tomatoes_client/query/parameters/browsing.py#L25-L34) like [`MovieBrowsingCategory.certified_fresh_in_theaters`](https://github.com/jaebradley/rotten_tomatoes_client/blob/master/rotten_tomatoes_client/query/parameters/browsing.py#L29).

```python
from rotten_tomatoes_client import RottenTomatoesClient, MovieBrowsingQuery, Service, Genre, SortBy, MovieBrowsingCategory

# Give me some relatively shitty action, comedy, or romance movies on Netflix or Amazon Prime, sorted by popularity
query = MovieBrowsingQuery(minimum_rating=35, maximum_rating=70, services=[Service.netflix, Service.amazon_prime],
                           certified_fresh=False, genres=[Genre.action, Genre.comedy, Genre.romance], sort_by=SortBy.popularity,
                           category=MovieBrowsingCategory.all_dvd_and_streaming)

result = RottenTomatoesClient.browse_movies(query=query)

# The result will look something like this
# {
#   "counts": {
#     "count": 32,
#     "total": 771
#   },
#   "results": [
#     {
#       "id": 10180,
#       "title": "10 Things I Hate About You",
#       "url": "/m/10_things_i_hate_about_you",
#       "tomatoIcon": "fresh",
#       "tomatoScore": 61,
#       "popcornIcon": "upright",
#       "popcornScore": 69,
#       "theaterReleaseDate": "Mar 31",
#       "dvdReleaseDate": "Oct 12",
#       "mpaaRating": "PG13",
#       "synopsis": "Julia Stiles and Heath Ledger add strong performances to an unexpectedly clever script, elevating 10 Things (slightly) above typical teen fare.",
#       "synopsisType": "consensus",
#       "runtime": "1 hr. 37 min.",
#       "posters": {
#         "thumborId": "v1.bTsxMTIwNzQ3NTtqOzE3NDA5OzEyMDA7MTgwMDsyNDAw",
#         "primary": "https://resizing.flixster.com/J0m170tQD8igSYaxp2rtyd5N8wU=/130x0/v1.bTsxMTIwNzQ3NTtqOzE3NDA5OzEyMDA7MTgwMDsyNDAw"
#       },
#       "actors": [
#         "Larisa Oleynik",
#         "Julia Stiles",
#         "Heath Ledger"
#       ]
#     },
#     {
#       "id": 12852,
#       "title": "Love Actually",
#       "url": "/m/love_actually",
#       "tomatoIcon": "fresh",
#       "tomatoScore": 63,
#       "popcornIcon": "upright",
#       "popcornScore": 72,
#       "theaterReleaseDate": "Nov 7",
#       "dvdReleaseDate": "Apr 27",
#       "mpaaRating": "R",
#       "synopsis": "A sugary tale overstuffed with too many stories. Still, the cast charms.",
#       "synopsisType": "consensus",
#       "runtime": "2 hr. 15 min.",
#       "mainTrailer": {
#         "sourceId": "http://link.theplatform.com/s/NGweTC/media/yHqz_0l_lb0V",
#         "id": "11295544"
#       },
#       "posters": {
#         "thumborId": "v1.bTsxMTE3NDgyMjtqOzE3NDA5OzEyMDA7ODAwOzEyMDA",
#         "primary": "https://resizing.flixster.com/V2-mrbEXdlXN269WjQ_pcuPpNXQ=/130x0/v1.bTsxMTE3NDgyMjtqOzE3NDA5OzEyMDA7ODAwOzEyMDA"
#       },
#       "actors": [
#         "Bill Nighy",
#         "Hugh Grant",
#         "Liam Neeson"
#       ]
#     },
#     {
#       "id": 2864421,
#       "title": "Hoodwinked",
#       "url": "/m/1155109-hoodwinked",
#       "tomatoIcon": "rotten",
#       "tomatoScore": 46,
#       "popcornIcon": "spilled",
#       "popcornScore": 56,
#       "theaterReleaseDate": "Jan 13",
#       "dvdReleaseDate": "May 2",
#       "mpaaRating": "PG",
#       "synopsis": "This fractured fairytale doesn't have the wit or animation quality to compete with the likes of the <i>Shrek</i> franchise.",
#       "synopsisType": "consensus",
#       "runtime": "1 hr. 20 min.",
#       "posters": {
#         "thumborId": "v1.bTsxMTIwOTMwNDtqOzE3NDA5OzEyMDA7MTUzNjsyMDQ4",
#         "primary": "https://resizing.flixster.com/Nra17Z2DFslffNklaVkXaGmSmw4=/130x0/v1.bTsxMTIwOTMwNDtqOzE3NDA5OzEyMDA7MTUzNjsyMDQ4"
#       },
#       "actors": [
#         "Glenn Close",
#         "Anne Hathaway",
#         "Jim Belushi"
#       ]
#     },
#     ...
#   ]
# }
```
