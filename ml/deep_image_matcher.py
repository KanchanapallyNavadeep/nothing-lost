from PIL import Image
import torch
import torch.nn.functional as F
from transformers import AutoImageProcessor, AutoModel


class DeepImageMatcher:

    def __init__(self):
        print("Loading AI image model...")

        self.model_name = "google/vit-base-patch16-224-in21k"

        self.processor = AutoImageProcessor.from_pretrained(
            self.model_name
        )

        self.model = AutoModel.from_pretrained(
            self.model_name
        )

        self.model.eval()

        print("AI image model loaded successfully.")

    def extract_features(self, image_path):

        image = Image.open(image_path).convert("RGB")

        inputs = self.processor(
            images=image,
            return_tensors="pt"
        )

        with torch.no_grad():

            outputs = self.model(**inputs)

        # Use the [CLS] token as the image representation
        features = outputs.last_hidden_state[:, 0, :]

        # Normalize embedding
        features = F.normalize(features, p=2, dim=1)

        return features

    def similarity(self, image1_path, image2_path):

        feature1 = self.extract_features(image1_path)
        feature2 = self.extract_features(image2_path)

        score = torch.sum(feature1 * feature2)

        return float(torch.clamp(score, 0.0, 1.0))