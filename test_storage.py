from backend.storage import load_data, save_data, add_lost_item, add_found_item


# Start with empty storage for this test
save_data({
    "lost_items": [],
    "found_items": []
})


lost_item = {
    "id": 1,
    "description": "Black leather wallet lost near library",
    "category": "wallet",
    "color": "black",
    "image": "images/lost_wallet (1).jpg",
    "latitude": 17.4360,
    "longitude": 78.3440
}


found_item = {
    "id": 101,
    "description": "Black leather wallet found near library",
    "category": "wallet",
    "color": "black",
    "image": "images/found_wallet (1).jpg",
    "latitude": 17.4370,
    "longitude": 78.3450
}


add_lost_item(lost_item)
add_found_item(found_item)


data = load_data()


print("\nSTORAGE TEST")
print("=" * 50)

print("\nLost items:")
print(data["lost_items"])

print("\nFound items:")
print(data["found_items"])