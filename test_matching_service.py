from backend.matching_service import find_matches


lost_item = {
    "id": 1,
    "description": "Black leather wallet lost near library",
    "category": "wallet",
    "color": "black",
    "image": "images/lost_wallet (1).jpg",
    "latitude": 17.4360,
    "longitude": 78.3440
}


results = find_matches(lost_item)


print("\nAI MATCHING SERVICE TEST")
print("=" * 60)

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