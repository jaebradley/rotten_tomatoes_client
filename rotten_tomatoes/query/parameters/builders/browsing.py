class MovieBrowsingQueryParametersBuilder:
    def __init__(self):
        pass

    @staticmethod
    def build(query):
        parameters = {
            "minTomato": query.minimum_rating,
            "maxTomato": query.maximum_rating,
            "certified": query.certified_fresh,
            "sort": query.sort_by.value,
            "type": query.category.value
        }

        if query.services is not None and len(query.services) > 0:
            parameters["services"] = ";".join([service.value for service in query.services])

        if query.genres is not None and len(query.genres) > 0:
            parameters["genres"] = ";".join([genre.value for genre in query.genres])

        return parameters
