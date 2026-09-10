from PIL import Image
import numpy as np


class ImageMatcher:
    def __init__(self, image_size=(128, 128)):
        self.image_size = image_size

    def extract_features(self, image_path):
        image = Image.open(image_path).convert("RGB")
        image = image.resize(self.image_size)

        pixels = np.asarray(image, dtype=np.float32) / 255.0

        features = pixels.flatten()
        norm = np.linalg.norm(features)

        if norm == 0:
            return features

        return features / norm

    def similarity(self, image1_path, image2_path):
        feature1 = self.extract_features(image1_path)
        feature2 = self.extract_features(image2_path)

        score = np.dot(feature1, feature2)

        return float(np.clip(score, 0.0, 1.0))