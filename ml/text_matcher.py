from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class TextMatcher:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            ngram_range=(1, 2)
        )

    def match(self, lost_description, found_descriptions):
        """
        Compare one lost-item description against multiple
        found-item descriptions.

        Returns a list of similarity scores between 0 and 1.
        """

        if not found_descriptions:
            return []

        documents = [lost_description] + found_descriptions

        vectors = self.vectorizer.fit_transform(documents)

        lost_vector = vectors[0]
        found_vectors = vectors[1:]

        scores = cosine_similarity(lost_vector, found_vectors)[0]

        return scores.tolist()