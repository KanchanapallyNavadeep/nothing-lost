from ml.text_matcher import TextMatcher
from ml.advanced_image_matcher import AdvancedImageMatcher
from ml.location_matcher import LocationMatcher


class LostFoundMatcher:

    def __init__(self):

        self.text_matcher = TextMatcher()
        self.image_matcher = AdvancedImageMatcher()
        self.location_matcher = LocationMatcher()

    def calculate_attribute_score(self, lost_item, found_item):

        scores = []

        if "category" in lost_item and "category" in found_item:

            scores.append(
                1.0
                if lost_item["category"].lower()
                == found_item["category"].lower()
                else 0.0
            )

        if "color" in lost_item and "color" in found_item:

            scores.append(
                1.0
                if lost_item["color"].lower()
                == found_item["color"].lower()
                else 0.0
            )

        return sum(scores) / len(scores) if scores else 0.0

    def calculate_location_score(self, lost_item, found_item):

        if (
            "latitude" not in lost_item
            or "longitude" not in lost_item
            or "latitude" not in found_item
            or "longitude" not in found_item
        ):
            return 0.0

        return self.location_matcher.similarity(
            lost_item["latitude"],
            lost_item["longitude"],
            found_item["latitude"],
            found_item["longitude"]
        )

    def match_items(self, lost_item, found_items):

        descriptions = [
            item["description"]
            for item in found_items
        ]

        text_scores = self.text_matcher.match(
            lost_item["description"],
            descriptions
        )

        results = []

        for item, text_score in zip(found_items, text_scores):

            # IMAGE SCORE
            image_score = 0.0

            if (
                lost_item.get("image")
                and item.get("image")
            ):

                image_score = self.image_matcher.similarity(
                    lost_item["image"],
                    item["image"]
                )

            # ATTRIBUTE SCORE
            attribute_score = self.calculate_attribute_score(
                lost_item,
                item
            )

            # LOCATION SCORE
            location_score = self.calculate_location_score(
                lost_item,
                item
            )

            # FINAL SCORE
            final_score = (
                0.40 * image_score +
                0.25 * float(text_score) +
                0.20 * location_score +
                0.15 * attribute_score
            )

            results.append({

                "id": item["id"],

                "description": item["description"],

                "image_score":
                    round(image_score, 4),

                "text_score":
                    round(float(text_score), 4),

                "location_score":
                    round(location_score, 4),

                "attribute_score":
                    round(attribute_score, 4),

                "final_score":
                    round(float(final_score), 4)
            })

        results.sort(
            key=lambda x: x["final_score"],
            reverse=True
        )

        return results