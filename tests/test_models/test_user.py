#!/usr/bin/python3
""" Unnitest for user.py """
import unittest
import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """Tests instances and methods from user class"""
    
    def test_initialization(self):
        user = User()
        self.assertTrue(isinstance(user, User))

    def test_default_attributes(self):
        user = User()
        self.assertEqual(user.email, '')
        self.assertEqual(user.password, '')
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')

    def test_attributes_with_values(self):
        user = User()
        user.email = 'user@example.com'
        user.password = 'password123'
        user.first_name = 'John'
        user.last_name = 'Doe'

        self.assertEqual(user.email, 'user@example.com')
        self.assertEqual(user.password, 'password123')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')


if __name__ == '__main__':
    unittest.main()
