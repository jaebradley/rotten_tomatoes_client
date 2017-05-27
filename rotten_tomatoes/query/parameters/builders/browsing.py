class MovieBrowsingQueryParametersBuilder:
    def __init__(self):
        pass

    @staticmethod
    def build(query):
        parameters = {
            "minTomato": query.minimum_rating,
            "maxTomato": query.maximum_rating,
            "certified": query.certified_fresh,
            "sort": query.sort_by,
            "type": query.category
        }

        if query.services is not None and len(query.services) > 0:
            parameters["services"] = ";".join([service for service in query.services])

        if query.genres is not None and len(query.genres) > 0:
            parameters["genres"] = ";".join([genre for genre in query.genres])

        return parameters
