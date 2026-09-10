from backend.models import FoundItem
from backend.storage import add_found_item


def register_found_item(item):

    found_item = FoundItem(
        id=item["id"],
        description=item["description"],
        category=item["category"],
        color=item["color"],
        image=item.get("image"),
        latitude=item.get("latitude"),
        longitude=item.get("longitude")
    )

    item_data = {
        "id": found_item.id,
        "description": found_item.description,
        "category": found_item.category,
        "color": found_item.color,
        "image": found_item.image,
        "latitude": found_item.latitude,
        "longitude": found_item.longitude
    }

    add_found_item(item_data)

    return item_data