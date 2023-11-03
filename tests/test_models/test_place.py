#!/usr/bin/python3
"""Unittest module for Place"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City


class TestPlace(unittest.TestCase):
    """class testing the Place class"""

    def test_initialization(self):
        place = Place()
        self.assertTrue(isinstance(place, Place))

    def test_default_attributes(self):
        place = Place()
        self.assertEqual(place.city_id, '')
        self.assertEqual(place.user_id, '')
        self.assertEqual(place.name, '')
        self.assertEqual(place.description, '')
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_attributes_with_values(self):
        place = Place()
        place.city_id = 'NYC'
        place.user_id = 'user123'
        place.name = 'Cozy Apartment'
        place.description = 'A comfortable place to stay.'
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 40.7128
        place.longitude = -74.0060
        place.amenity_ids = ['wifi', 'pool', 'parking']

        self.assertEqual(place.city_id, 'NYC')
        self.assertEqual(place.user_id, 'user123')
        self.assertEqual(place.name, 'Cozy Apartment')
        self.assertEqual(place.description, 'A comfortable place to stay.')
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertEqual(place.amenity_ids, ['wifi', 'pool', 'parking'])


if __name__ == '__main__':
    unittest.main()
