import unittest
from data_processor import classify_rating

class TestFeedbackProcessor(unittest.TestCase):
    def test_classify_rating(self):
        self.assertEqual(classify_rating(5), "positive")
        self.assertEqual(classify_rating(4), "positive")
        self.assertEqual(classify_rating(3), "neutral")
        self.assertEqual(classify_rating(2), "negative")
        self.assertEqual(classify_rating(1), "negative")

if __name__ == "__main__":
    unittest.main()
