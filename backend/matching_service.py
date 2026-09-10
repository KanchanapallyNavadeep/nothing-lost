from ml.matcher import LostFoundMatcher
from backend.storage import load_data


matcher = LostFoundMatcher()


def find_matches(lost_item):

    data = load_data()

    found_items = data["found_items"]

    if not found_items:
        return []

    results = matcher.match_items(
        lost_item,
        found_items
    )

    return results