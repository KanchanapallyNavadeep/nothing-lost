from ml.image_matcher import ImageMatcher

matcher = ImageMatcher()

image1 = "images/lost_wallet (1).jpg"
image2 = "images/found_wallet (1).jpg"

score = matcher.similarity(image1, image2)

print("Image similarity:", score)