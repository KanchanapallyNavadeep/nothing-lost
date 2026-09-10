from backend.found_item_service import register_found_item
from backend.storage import load_data


found_item = {
    "id": 102,
    "description": "Blue backpack found near college gate",
    "category": "backpack",
    "color": "blue",
    "image": None,
    "latitude": 17.4400,
    "longitude": 78.3500
}


registered_item = register_found_item(found_item)


print("\nFOUND ITEM REGISTRATION TEST")
print("=" * 50)

print("\nRegistered item:")
print(registered_item)


data = load_data()

print("\nTotal found items:", len(data["found_items"]))

print("\nLatest found item:")
print(data["found_items"][-1])