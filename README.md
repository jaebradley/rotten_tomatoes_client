[![Build Status](https://travis-ci.com/Genza999/rotten_tomatoes_client.svg?branch=task/update_readme)](https://travis-ci.com/Genza999/rotten_tomatoes_client)
[![PyPI version](https://badge.fury.io/py/rotten_tomatoes_client.svg)](https://badge.fury.io/py/rotten_tomatoes_client)
[![codecov](https://codecov.io/gh/Genza999/rotten_tomatoes_client/branch/task/update_readme/graph/badge.svg?token=8BSTNZW3F7)](https://codecov.io/gh/Genza999/rotten_tomatoes_client)

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
* `page`
  * The page of the results to be returned.
  * Defaults to page `1` i.e. the first page.
* `limit`
  * The maximum number of results to be returned.
  * Defaults to `32`
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


### Movie Details

The [`movie details` method](https://github.com/jaebradley/rotten_tomatoes_client/blob/master/rotten_tomatoes_client/client.py#L44-L51) takes a `movie_id` parameter to search for full details about a movie.
* `movie_id`
  * ID of the movie whose details are to be returned

```python
from rotten_tomatoes_client import RottenTomatoesClient

result = RottenTomatoesClient.get_movie_details(movie_id=446064253)

# The result will look something like this
# {
#    "studio":"Asmik Ace Entertainment",
#    "isInTheaters":false,
#    "adjustedScore":36.425650280643076,
#    "ratingSummary":{
#       "topCritics":{
#          "averageRating":7.25,
#          "meterValue":100,
#          "numReviews":5,
#          "meterClass":"fresh",
#          "numRotten":0,
#          "hasScore":true,
#          "hasReviews":true,
#          "numFresh":5
#       },
#       "audience":{
#          "numTotal":3368,
#          "averageScore":4.303986549377441,
#          "ratingType":"viewed",
#          "meterScore":93
#       },
#       "allcount":12,
#       "freshcount":11,
#       "dvdcount":0,
#       "consensus":"No consensus yet.",
#       "allCritics":{
#          "averageRating":7.92,
#          "meterValue":100,
#          "numReviews":11,
#          "meterClass":"fresh",
#          "numRotten":0,
#          "hasScore":true,
#          "hasReviews":true,
#          "numFresh":11
#       },
#       "rottencount":0,
#       "topcount":5
#    },
#    "isPlaying":false,
#    "id":446064253,
#    "title":"Mind Game",
#    "vanity":"mind-game",
#    "officialUrl":"http://www.mindgame.jp/",
#    "advisory":"",
#    "synopsis":"Cult classic Mind Game is an explosion of unconstrained expression - gloriously colorful mages ricochet in rapid fire associations, like Masaaki Yuasa's brain splattered onto the screen in all its goopy glory. Audiences will begin to grasp what they are in for early on as loser Nishi, too wimpy to try to save his childhood sweetheart from gangsters, is shot in the butt by a soccer-playing psychopath, projecting Nishi into the afterlife. In this limbo, God - shown as a series of rapidly changing characters - tells him to walk toward the light. But Nishi runs like hell in the other direction and returns to Earth a changed man, driven to live each moment to the fullest.",
#    "casts":{
#       "creators":[
         
#       ],
#       "castItems":[
#          {
#             "person":{
#                "name":"Sayaka Maeda",
#                "thumbnailImg":"https://d2a5cgar23scu2.cloudfront.net/static/images/redesign/actor.default.tmb.gif",
#                "url":"/celebrity/sayaka_maeda/"
#             },
#             "characters":[
#                {
#                   "name":"Myon"
#                }
#             ]
#          },
#          {
#             "person":{
#                "name":"Seiko Takuma",
#                "thumbnailImg":"https://d2a5cgar23scu2.cloudfront.net/static/images/redesign/actor.default.tmb.gif",
#                "url":"/celebrity/seiko_takuma/"
#             },
#             "characters":[
#                {
#                   "name":"Yan"
#                }
#             ]
#          },
#          {
#             "person":{
#                "name":"Tomomitsu Yamaguchi",
#                "thumbnailImg":"https://d2a5cgar23scu2.cloudfront.net/static/images/redesign/actor.default.tmb.gif",
#                "url":"/celebrity/tomomitsu_yamaguchi/"
#             },
#             "characters":[
#                {
#                   "name":"Ry?"
#                }
#             ]
#          },
#          {
#             "person":{
#                "name":"Takashi Fujii",
#                "thumbnailImg":"https://d2a5cgar23scu2.cloudfront.net/static/images/redesign/actor.default.tmb.gif",
#                "url":"/celebrity/takashi_fujii/"
#             },
#             "characters":[
#                {
#                   "name":"Old"
#                }
#             ]
#          },
#          {
#             "person":{
#                "name":"Koji Imada",
#                "thumbnailImg":"https://d2a5cgar23scu2.cloudfront.net/static/images/redesign/actor.default.tmb.gif",
#                "url":"/celebrity/koji_imada/"
#             },
#             "characters":[
#                {
#                   "name":"Nishi"
#                }
#             ]
#          }
#       ],
#       "screenwriters":[
#          {
#             "name":"Masaaki Yuasa",
#             "thumbnailImg":"https://resizing.flixster.com/IsT4o8cLK3g78p9z0h7-7RI1TxE=/80x80/v1.cDs2MjE3ODc3O2o7MTg4ODM7MjA0ODsxMDA7MTAw",
#             "url":"/celebrity/masaaki_yuasa/"
#          }
#       ],
#       "directors":[
#          {
#             "name":"Masaaki Yuasa",
#             "thumbnailImg":"https://resizing.flixster.com/IsT4o8cLK3g78p9z0h7-7RI1TxE=/80x80/v1.cDs2MjE3ODc3O2o7MTg4ODM7MjA0ODsxMDA7MTAw",
#             "url":"/celebrity/masaaki_yuasa/"
#          }
#       ],
#       "producers":[
#          {
#             "name":"Eiko Tanaka",
#             "thumbnailImg":"https://d2a5cgar23scu2.cloudfront.net/static/images/redesign/actor.default.tmb.gif",
#             "url":"/celebrity/eiko_tanaka/"
#          }
#       ]
#    },
#    "mainTrailer":{
#       "id":11305753,
#       "thumbUrl":"https://resizing.flixster.com/sdZuIBXYOk_8q4S2DcMi8jCEMtk=/171x128/v1.bjsxODg0NjI1O2o7MTg4NzY7MjA0ODsxMDgwOzE5MjA",
#       "mp4Url":"http://video.internetvideoarchive.net/video.mp4?cmd=6&publishedid=http://link.theplatform.com/s/NGweTC/media/E0S5iwhykpeK&customerid=300120&e=1624354006884&sub=RTO&fmt=4&videokbrate=750&h=d947256341c3985fa2962e0c4a34a6d2",
#       "hlsUrl":"http://video.internetvideoarchive.net/video.m3u8?cmd=6&publishedid=http://link.theplatform.com/s/NGweTC/media/E0S5iwhykpeK&customerid=300120&e=1624354006884&sub=RTO&fmt=11&h=26cd3343a50836cfcd3d7ac986de7d33"
#    },
#    "isOnDVD":true,
#    "year":2004,
#    "trackingType":"DvdOther",
#    "genreSet":[
#       {
#          "id":1,
#          "displayName":"Action & Adventure"
#       },
#       {
#          "id":2,
#          "displayName":"Animation"
#       },
#       {
#          "id":4,
#          "displayName":"Art House & International"
#       },
#       {
#          "id":14,
#          "displayName":"Science Fiction & Fantasy"
#       },
#       {
#          "id":6,
#          "displayName":"Comedy"
#       }
#    ],
#    "isUpcoming":false,
#    "reviews":{
#       "total":12,
#       "reviews":[
#          {
#             "id":2461719,
#             "creationDate":1520006956000,
#             "isRotten":false,
#             "quote":"Just relax, and let Yuasa take you wherever the hell he wants.",
#             "links":{
#                "review":"https://www.villagevoice.com/2018/03/01/it-is-hard-to-describe-the-glorious-nuttiness-of-mind-game/"
#             },
#             "freshness":"fresh",
#             "isTop":true,
#             "url":"https://www.villagevoice.com/2018/03/01/it-is-hard-to-describe-the-glorious-nuttiness-of-mind-game/",
#             "isFresh":true,
#             "critic":{
#                "id":13027,
#                "name":"Simon Abrams",
#                "thumbnailImage":"https://d2a5cgar23scu2.cloudfront.net/static/images/redesign/user.none.tmb.jpg",
#                "url":"/critic/simon-abrams"
#             },
#             "publication":{
#                "name":"Village Voice",
#                "url":""
#             }
#          },
#          {
#             "id":1809060,
#             "creationDate":1238148945000,
#             "isRotten":false,
#             "quote":"With imaginative handling, this freewheeling juggernaut of a head-trip, its assorted visual treatments rendered in relative degrees of awkwardness and artfulness, could catch on with hip auds worldwide.",
#             "links":{
#                "review":"http://www.variety.com/review/VE1117927691.html?categoryid=31&cs=1"
#             },
#             "freshness":"fresh",
#             "isTop":true,
#             "url":"http://www.variety.com/review/VE1117927691.html?categoryid=31&cs=1",
#             "isFresh":true,
#             "critic":{
#                "id":12109,
#                "name":"Ronnie Scheib",
#                "thumbnailImage":"https://d2a5cgar23scu2.cloudfront.net/static/images/redesign/user.none.tmb.jpg",
#                "url":"/critic/ronnie-scheib"
#             },
#             "publication":{
#                "name":"Variety",
#                "url":""
#             }
#          },
#          {
#             "id":1532127,
#             "creationDate":1155809782000,
#             "isRotten":false,
#             "quote":"A fantastically executed assemblage of animated flotsam punctuated with moments of dry humour and a heartbreaking final montage which gives the film its message - make every moment count.",
#             "links":{
#                "review":"http://www.timeout.com/film/83664.html"
#             },
#             "freshness":"fresh",
#             "isTop":true,
#             "url":"http://www.timeout.com/film/83664.html",
#             "isFresh":true,
#             "critic":{
#                "id":12304,
#                "name":"David Jenkins",
#                "thumbnailImage":"https://d2a5cgar23scu2.cloudfront.net/static/images/redesign/user.none.tmb.jpg",
#                "url":"/critic/david-jenkins"
#             },
#             "publication":{
#                "name":"Time Out",
#                "url":""
#             }
#          },
#          {
#             "id":1431851,
#             "creationDate":1125620001000,
#             "isRotten":false,
#             "original_score":"3.5/5",
#             "quote":"A sometimes enthralling, sometimes exhausting tour de force.",
#             "links":{
               
#             },
#             "freshness":"fresh",
#             "isTop":true,
#             "isFresh":true,
#             "critic":{
#                "id":988,
#                "name":"A.O. Scott",
#                "thumbnailImage":"https://resizing.flixster.com/IbD1oOkwETagB5IqM09B_xf_wEI=/72x72/v1.YzszNjI4O2o7MTg4Mzg7MjA0ODszMDA7MzAw",
#                "url":"/critic/ao-scott"
#             },
#             "publication":{
#                "name":"New York Times",
#                "url":""
#             }
#          },
#          {
#             "id":1431306,
#             "creationDate":1125443809000,
#             "isRotten":false,
#             "quote":"A virtuoso narrative loop-the-loop that travels through a phantasmagoric catalog of animation styles.",
#             "links":{
#                "review":"http://www.villagevoice.com/film/0535,tracking1,67306,20.html"
#             },
#             "freshness":"fresh",
#             "isTop":true,
#             "url":"http://www.villagevoice.com/film/0535,tracking1,67306,20.html",
#             "isFresh":true,
#             "critic":{
#                "id":5497,
#                "name":"Ed Halter",
#                "thumbnailImage":"https://d2a5cgar23scu2.cloudfront.net/static/images/redesign/user.none.tmb.jpg",
#                "url":"/critic/ed-halter"
#             },
#             "publication":{
#                "name":"Village Voice",
#                "url":""
#             }
#          },
#          {
#             "id":2734551,
#             "creationDate":1602805681000,
#             "isRotten":false,
#             "quote":"...no end of phantasmagorical weirdness...",
#             "links":{
#                "review":"https://48hills.org/2018/03/screen-grabs-foxtrot-mind-game-drag-hell/"
#             },
#             "freshness":"fresh",
#             "isTop":false,
#             "url":"https://48hills.org/2018/03/screen-grabs-foxtrot-mind-game-drag-hell/",
#             "isFresh":true,
#             "critic":{
#                "id":3084,
#                "name":"Dennis Harvey",
#                "thumbnailImage":"https://d2a5cgar23scu2.cloudfront.net/static/images/redesign/user.none.tmb.jpg",
#                "url":"/critic/dennis-harvey"
#             },
#             "publication":{
#                "name":"48 Hills",
#                "url":""
#             }
#          },
#          {
#             "id":2514899,
#             "creationDate":1538591834000,
#             "isRotten":false,
#             "original_score":"4/5",
#             "quote":"Cult-classic anime has lots of violence, language. ",
#             "links":{
#                "review":"https://www.commonsensemedia.org/movie-reviews/mind-game"
#             },
#             "freshness":"fresh",
#             "isTop":false,
#             "url":"https://www.commonsensemedia.org/movie-reviews/mind-game",
#             "isFresh":true,
#             "critic":{
#                "id":14235,
#                "name":"Brian Costello",
#                "thumbnailImage":"https://d2a5cgar23scu2.cloudfront.net/static/images/redesign/user.none.tmb.jpg",
#                "url":"/critic/brian-costello"
#             },
#             "publication":{
#                "name":"Common Sense Media",
#                "url":""
#             }
#          },
#          {
#             "id":2487451,
#             "creationDate":1530211415000,
#             "isRotten":false,
#             "quote":"But for all the insanity-smoking koi, giant talking flowers living on dinosaur poop... there's also a beautiful poetry to Mind Game.",
#             "links":{
#                "review":"https://www.straight.com/movies/1095471/mind-game-some-sort-demented-anime-classic"
#             },
#             "freshness":"fresh",
#             "isTop":false,
#             "url":"https://www.straight.com/movies/1095471/mind-game-some-sort-demented-anime-classic",
#             "isFresh":true,
#             "critic":{
#                "id":10911,
#                "name":"Mike Usinger",
#                "thumbnailImage":"https://d2a5cgar23scu2.cloudfront.net/static/images/redesign/user.none.tmb.jpg",
#                "url":"/critic/mike-usinger"
#             },
#             "publication":{
#                "name":"Georgia Straight",
#                "url":""
#             }
#          },
#          {
#             "id":2265455,
#             "creationDate":1433407379000,
#             "isRotten":false,
#             "original_score":"9/10",
#             "quote":"One of the essential animated features in the last 15 years.",
#             "links":{
#                "review":"http://antagonie.blogspot.com/2015/05/point-of-view.html"
#             },
#             "freshness":"fresh",
#             "isTop":false,
#             "url":"http://antagonie.blogspot.com/2015/05/point-of-view.html",
#             "isFresh":true,
#             "critic":{
#                "id":12682,
#                "name":"Tim Brayton",
#                "thumbnailImage":"https://resizing.flixster.com/CdBAy1NfW--gmtqLvUa0KknlFck=/72x72/v1.YzszODU2O2o7MTg4NDE7MjA0ODszMDA7MzAw",
#                "url":"/critic/tim-brayton"
#             },
#             "publication":{
#                "name":"Antagony & Ecstasy"
#             }
#          },
#          {
#             "id":1432214,
#             "creationDate":1125699279000,
#             "isRotten":false,
#             "original_score":"3/5",
#             "quote":"If the film's pop-psychedelic noodling about fate, self-determination and the power of love looks muzzy-headed on closer consideration, its dense barrage of images richly repays second and third viewings.",
#             "links":{
               
#             },
#             "freshness":"fresh",
#             "isTop":false,
#             "isFresh":true,
#             "critic":{
#                "id":1179,
#                "name":"Maitland McDonagh",
#                "thumbnailImage":"https://resizing.flixster.com/UT3jy0gsAbso2wzfUjSChuRCLtw=/72x72/v1.YzsxNjQ4O2c7MTg4Mzg7MjA0ODszODs1Mw",
#                "url":"/critic/maitland-mcdonagh"
#             },
#             "publication":{
#                "name":"TV Guide",
#                "url":""
#             }
#          },
#          {
#             "id":1431760,
#             "creationDate":1125602920000,
#             "isRotten":false,
#             "original_score":"5/5",
#             "quote":"The best animated film of the year.",
#             "links":{
               
#             },
#             "freshness":"fresh",
#             "isTop":false,
#             "isFresh":true,
#             "critic":{
#                "id":2920,
#                "name":"Phil Hall",
#                "thumbnailImage":"https://resizing.flixster.com/hzueFqf2MOEvpLV50kOKUim8qL4=/72x72/v1.YzsxNjgzO2c7MTg4Mjg7MjA0ODszODs0Mg",
#                "url":"/critic/phil-hall"
#             },
#             "publication":{
#                "name":"Film Threat",
#                "url":""
#             }
#          },
#          {
#             "id":1615093,
#             "creationDate":1176804927000,
#             "isRotten":false,
#             "links":{
#                "review":"http://www.twitchfilm.net/archives/002668.html"
#             },
#             "freshness":"none",
#             "isTop":false,
#             "url":"http://www.twitchfilm.net/archives/002668.html",
#             "isFresh":false,
#             "publication":{
#                "name":"ScreenAnarchy",
#                "url":""
#             }
#          }
#       ],
#       "links":{
#          "alternate":"//www.rottentomatoes.com/m/mind-game/#reviews",
#          "self":"api.flixster.com/movies/mind-game/reviews.json?review_type=mob&country=us"
#       }
#    },
#    "status":"Live",
#    "mpaaRating":"Unrated",
#    "purchaseOptions":{
#       "netflix":{
#          "streamingId":"80063295"
#       }
#    },
#    "links":{
#       "alternate":"//www.rottentomatoes.com/m/mind-game/"
#    },
#    "videoClips":{
#       "mainTrailer":{
#          "id":11305753,
#          "title":"Mind Game: US Release Trailer",
#          "minutes":1,
#          "seconds":41,
#          "thumbUrl":"http://resizing.flixster.com/sdZuIBXYOk_8q4S2DcMi8jCEMtk=/171x128/v1.bjsxODg0NjI1O2o7MTg4NzY7MjA0ODsxMDgwOzE5MjA",
#          "mp4Url":"http://video.internetvideoarchive.net/video.mp4?cmd=6&publishedid=http://link.theplatform.com/s/NGweTC/media/E0S5iwhykpeK&customerid=300120&e=1624354007081&sub=RTO&fmt=4&videokbrate=750&h=201cb463c02b8b5fae021a621a44fe29",
#          "hlsUrl":"http://video.internetvideoarchive.net/video.m3u8?cmd=6&publishedid=http://link.theplatform.com/s/NGweTC/media/E0S5iwhykpeK&customerid=300120&e=1624354007081&sub=RTO&fmt=11&h=137f90745565ff4d05393c76b883314a"
#       },
#       "videoClips":[
#          {
#             "id":11305753,
#             "title":"Mind Game: US Release Trailer",
#             "minutes":1,
#             "seconds":41,
#             "thumbUrl":"http://resizing.flixster.com/sdZuIBXYOk_8q4S2DcMi8jCEMtk=/171x128/v1.bjsxODg0NjI1O2o7MTg4NzY7MjA0ODsxMDgwOzE5MjA",
#             "mp4Url":"http://video.internetvideoarchive.net/video.mp4?cmd=6&publishedid=http://link.theplatform.com/s/NGweTC/media/E0S5iwhykpeK&customerid=300120&e=1624354007081&sub=RTO&fmt=4&videokbrate=750&h=201cb463c02b8b5fae021a621a44fe29",
#             "hlsUrl":"http://video.internetvideoarchive.net/video.m3u8?cmd=6&publishedid=http://link.theplatform.com/s/NGweTC/media/E0S5iwhykpeK&customerid=300120&e=1624354007081&sub=RTO&fmt=11&h=137f90745565ff4d05393c76b883314a"
#          }
#       ],
#       "size":1
#    },
#    "runningTime":104,
#    "runningTimeStr":"1 hr. 44 min.",
#    "url":"/m/mind-game/",
#    "photos":{
#       "photos":[
#          {
#             "id":"multiuse-1852922",
#             "photoType":"movie",
#             "index":0,
#             "imageId":1852922,
#             "thumbnail":"https://resizing.flixster.com/FATu3Sn3WJ3CVtUq4F3cpPTojUM=/80x80/v1.bjsxODUyOTIyO2o7MTg4Nzg7MjA0ODsxNDQwOzYxMg",
#             "height":435,
#             "width":1024,
#             "submittedDate":"2018-02-12",
#             "submittedBy":"RT Staff",
#             "url":"https://resizing.flixster.com/v6xAg79Sw4QPkUCoT_Hlz_H6yPI=/1024x435/v1.bjsxODUyOTIyO2o7MTg4Nzg7MjA0ODsxNDQwOzYxMg"
#          },
#          {
#             "id":"multiuse-1852924",
#             "photoType":"movie",
#             "index":1,
#             "imageId":1852924,
#             "thumbnail":"https://resizing.flixster.com/dOH0NIdnXRUAfvLJZODOQhxLYIM=/80x80/v1.bjsxODUyOTI0O2o7MTg4ODA7MjA0ODsxNDQwOzYxMg",
#             "height":435,
#             "width":1024,
#             "submittedDate":"2018-02-12",
#             "submittedBy":"RT Staff",
#             "url":"https://resizing.flixster.com/vbmG16qQVTKoA26uWmkzh5SzDUs=/1024x435/v1.bjsxODUyOTI0O2o7MTg4ODA7MjA0ODsxNDQwOzYxMg"
#          },
#          {
#             "id":"multiuse-1852925",
#             "photoType":"movie",
#             "index":2,
#             "imageId":1852925,
#             "thumbnail":"https://resizing.flixster.com/wyDVrlJrEG_WzYV6dwO8hRwnnUc=/80x80/v1.bjsxODUyOTI1O2o7MTg4ODE7MjA0ODsxNDQwOzYxMg",
#             "height":435,
#             "width":1024,
#             "submittedDate":"2018-02-12",
#             "submittedBy":"RT Staff",
#             "url":"https://resizing.flixster.com/yu6O1QAwAyNPy4Z3OLTMsZ5rsg0=/1024x435/v1.bjsxODUyOTI1O2o7MTg4ODE7MjA0ODsxNDQwOzYxMg"
#          },
#          {
#             "id":"multiuse-1852926",
#             "photoType":"movie",
#             "index":3,
#             "imageId":1852926,
#             "thumbnail":"https://resizing.flixster.com/ULHboseXA2Lt_Hbu4vHPRgeSDJ0=/80x80/v1.bjsxODUyOTI2O2o7MTg4ODI7MjA0ODsxNDQwOzYxMg",
#             "height":435,
#             "width":1024,
#             "submittedDate":"2018-02-12",
#             "submittedBy":"RT Staff",
#             "url":"https://resizing.flixster.com/lqQHDnYkdRfjODvjSHEOXduz1q0=/1024x435/v1.bjsxODUyOTI2O2o7MTg4ODI7MjA0ODsxNDQwOzYxMg"
#          },
#          {
#             "id":"multiuse-1852923",
#             "photoType":"movie",
#             "index":4,
#             "imageId":1852923,
#             "thumbnail":"https://resizing.flixster.com/f5fip98pjgF-SIsQaJ9Hux6nrQM=/80x80/v1.bjsxODUyOTIzO2o7MTg4Nzk7MjA0ODsxNDQwOzYxMg",
#             "height":435,
#             "width":1024,
#             "submittedDate":"2018-02-12",
#             "submittedBy":"RT Staff",
#             "url":"https://resizing.flixster.com/k8D7FSeXAMp7PUsoUwWK-A7ko1s=/1024x435/v1.bjsxODUyOTIzO2o7MTg4Nzk7MjA0ODsxNDQwOzYxMg"
#          }
#       ],
#       "length":5
#    },
#    "isOnOpening":false,
#    "isLimited":false,
#    "posters":{
#       "thumbnail":"https://resizing.flixster.com/GUaxeHmFv869TY3GR2tpY6aVSOI=/54x72/v1.bTsxMTIxNjYyODtqOzE4OTEyOzIwNDg7MTUwMDsyMDAw",
#       "detailed":"https://resizing.flixster.com/0KwaGqk5NWqYYHM5PHAJcR4ahFA=/180x240/v1.bTsxMTIxNjYyODtqOzE4OTEyOzIwNDg7MTUwMDsyMDAw",
#       "original":"https://resizing.flixster.com/HbfQRJf39N9LGdL7lrFj8yPGz7A=/1500x2000/v1.bTsxMTIxNjYyODtqOzE4OTEyOzIwNDg7MTUwMDsyMDAw",
#       "profile":"https://resizing.flixster.com/_UJjdG8fEwEhBcxS5fEZlK8aFnQ=/120x160/v1.bTsxMTIxNjYyODtqOzE4OTEyOzIwNDg7MTUwMDsyMDAw"
#    },
#    "ratings":{
#       "theaterReleaseDate":1091862000000,
#       "critics_score":100,
#       "critics_rating":"Fresh",
#       "dvdReleaseDate":1535439600000,
#       "audience_score":93,
#       "audience_rating":"Upright"
#    }
# }

