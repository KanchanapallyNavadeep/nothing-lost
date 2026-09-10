from math import radians, sin, cos, sqrt, atan2


class LocationMatcher:
    def __init__(self, max_distance_km=10):
        self.max_distance_km = max_distance_km

    def calculate_distance(self, lat1, lon1, lat2, lon2):
        """
        Calculate distance between two GPS coordinates
        using the Haversine formula.
        """

        earth_radius_km = 6371.0

        lat1 = radians(lat1)
        lon1 = radians(lon1)
        lat2 = radians(lat2)
        lon2 = radians(lon2)

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = (
            sin(dlat / 2) ** 2
            + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        )

        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        return earth_radius_km * c

    def similarity(self, lat1, lon1, lat2, lon2):
        """
        Convert geographical distance into a similarity score
        between 0 and 1.
        """

        distance = self.calculate_distance(
            lat1, lon1, lat2, lon2
        )

        if distance >= self.max_distance_km:
            return 0.0

        score = 1 - (distance / self.max_distance_km)

        return round(score, 4)