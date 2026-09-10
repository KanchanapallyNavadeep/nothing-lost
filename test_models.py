from backend.models import LostItem, FoundItem


lost_item = LostItem(
    id=1,
    description="Black leather wallet lost near library",
    category="wallet",
    color="black",
    image="images/lost_wallet (1).jpg",
    latitude=17.4360,
    longitude=78.3440
)


found_item = FoundItem(
    id=101,
    description="Black leather wallet found near library",
    category="wallet",
    color="black",
    image="images/found_wallet (1).jpg",
    latitude=17.4370,
    longitude=78.3450
)


print("\nDATA MODEL TEST")
print("=" * 50)

print("\nLOST ITEM")
print(lost_item)

print("\nFOUND ITEM")
print(found_item)