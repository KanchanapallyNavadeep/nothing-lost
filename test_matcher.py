from ml.matcher import LostFoundMatcher


matcher = LostFoundMatcher()


lost_item = {
    "id": 1,
    "description": "Black leather wallet lost near library",
    "category": "wallet",
    "color": "black",
    "image": "images/lost_wallet (1).jpg",
    "latitude": 17.4360,
    "longitude": 78.3440
}


found_items = [

    {
        "id": 101,
        "description": "Black leather wallet found near library",
        "category": "wallet",
        "color": "black",
        "image": "images/found_wallet (1).jpg",
        "latitude": 17.4370,
        "longitude": 78.3450
    },

    {
        "id": 102,
        "description": "Black backpack found near college gate",
        "category": "backpack",
        "color": "black",
        "image": None,
        "latitude": 17.4500,
        "longitude": 78.3600
    },

    {
        "id": 103,
        "description": "Brown leather purse found near library",
        "category": "purse",
        "color": "brown",
        "image": None,
        "latitude": 17.5000,
        "longitude": 78.4000
    }
]


results = matcher.match_items(
    lost_item,
    found_items
)


print("\nMATCH RESULTS")
print("=" * 50)

for result in results:

    print(
        f"\nID: {result['id']}"
        f"\nDescription: {result['description']}"
        f"\nImage Score: {result['image_score'] * 100:.2f}%"
        f"\nText Score: {result['text_score'] * 100:.2f}%"
        f"\nLocation Score: {result['location_score'] * 100:.2f}%"
        f"\nAttribute Score: {result['attribute_score'] * 100:.2f}%"
        f"\nFINAL SCORE: {result['final_score'] * 100:.2f}%"
    )