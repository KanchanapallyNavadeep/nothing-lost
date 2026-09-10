from ml.location_matcher import LocationMatcher


matcher = LocationMatcher(max_distance_km=10)

lost_location = (17.4360, 78.3440)

test_locations = [
    ("Very close", 17.4365, 78.3445),
    ("Nearby", 17.4400, 78.3480),
    ("Far", 17.5000, 78.4000),
    ("Very far", 17.6000, 78.5000),
]

for name, lat, lon in test_locations:

    distance = matcher.calculate_distance(
        lost_location[0],
        lost_location[1],
        lat,
        lon
    )

    score = matcher.similarity(
        lost_location[0],
        lost_location[1],
        lat,
        lon
    )

    print(
        f"{name}: "
        f"{distance:.3f} km -> "
        f"{score * 100:.2f}%"
    )