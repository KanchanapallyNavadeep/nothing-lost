from ml.text_matcher import TextMatcher


matcher = TextMatcher()

lost_item = "Black leather wallet lost near college library"

found_items = [
    "Black leather wallet found near library",
    "Blue water bottle found in classroom",
    "Black backpack found near college gate",
    "Brown leather purse found near library"
]

scores = matcher.match(lost_item, found_items)

for item, score in zip(found_items, scores):
    print(f"{score:.2f}  ->  {item}")