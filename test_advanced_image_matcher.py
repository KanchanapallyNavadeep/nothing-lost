from ml.advanced_image_matcher import AdvancedImageMatcher


matcher = AdvancedImageMatcher()


image1 = "images/lost_wallet (1).jpg"
image2 = "images/found_wallet (1).jpg"


score = matcher.similarity(
    image1,
    image2
)


print("\nADVANCED AI IMAGE MATCH")
print("=" * 50)

print(f"Image 1: {image1}")
print(f"Image 2: {image2}")

print(f"CLIP Similarity: {score * 100:.2f}%")