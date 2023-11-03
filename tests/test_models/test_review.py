#!/usr/bin/python3
"Unit tests for Review class"
import unittest
from models.review import Review
from models.place import Place


class TestReview(unittest.TestCase):
    "Unit tests suite for Review class"

    def test_initialization(self):
        review = Review()
        self.assertTrue(isinstance(review, Review))

    def test_default_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, '')
        self.assertEqual(review.user_id, '')
        self.assertEqual(review.text, '')

    def test_attributes_with_values(self):
        review = Review()
        review.place_id = 'place123'
        review.user_id = 'user123'
        review.text = 'A great place to stay!'

        self.assertEqual(review.place_id, 'place123')
        self.assertEqual(review.user_id, 'user123')
        self.assertEqual(review.text, 'A great place to stay!')


if __name__ == '__main__':
    unittest.main()
