#!/usr/bin/python3
""" Unit test for Amenity """
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    "Unit tests suite for Amenity class"

    def test_initialization(self):
        amenity = Amenity()
        self.assertTrue(isinstance(amenity, Amenity))

    def test_name_attribute(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, '')

    def test_name_attribute_with_value(self):
        amenity = Amenity()
        amenity.name = 'Swimming Pool'
        self.assertEqual(amenity.name, 'Swimming Pool')


if __name__ == '__main__':
    unittest.main()
