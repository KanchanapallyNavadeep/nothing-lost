from ml.image_matcher import ImageMatcher


matcher = ImageMatcher()

score = matcher.similarity(
    "images/lost_wallet.jpg",
    "images/found_wallet.jpg"
)

print(f"Image similarity: {score:.2f}")