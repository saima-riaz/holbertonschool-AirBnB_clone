import unittest
from unittest.mock import patch
from datetime import datetime
from models.base_model import BaseModel
""" Import the BaseModel class from your actual module """


class TestBaseModel(unittest.TestCase):

    @patch('models.base_model.datetime')
    def test_init(self, mock_datetime):
        """ Mock the current date and time for testing """
        mock_now = datetime(2023, 10, 31, 12, 0, 0)
        mock_datetime.now.return_value = mock_now

        """  Create an instance of the BaseModel class """
        base_model = BaseModel()

        """  Check that the instance has a non-empty ID
            the correct creation and update timestamps """
        self.assertIsNotNone(base_model.id)
        self.assertEqual(base_model.created_at, mock_now)
        self.assertEqual(base_model.updated_at, mock_now)

    def test_save(self):
        """  Create an instance of the BaseModel class """
        base_model = BaseModel()
        """ Store the original 'updated_at' timestamp """
        original_updated_at = base_model.updated_at
        """ Call the 'save' method to update the 'updated_at' timestamp """
        base_model.save()
        """ Check that 'updated_at' has been updated """
        self.assertNotEqual(base_model.updated_at, original_updated_at)

    def test_to_dict(self):
        """ convert the instance to a dictionary """
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()

        """ Check if the necessary keys are present in the dictionary """
        self.assertTrue('__class__' in base_model_dict)
        self.assertTrue('created_at' in base_model_dict)
        self.assertTrue('updated_at' in base_model_dict)

    def test_str(self):
        """ convert the instance to a string representation """
        base_model = BaseModel()
        obj_str = str(base_model)

        """ Check if the class name and ID are present
             in the string representation """
        self.assertTrue(base_model.__class__.__name__ in obj_str)
        self.assertTrue(base_model.id in obj_str)

    def test_init_with_kwargs(self):
        kwargs = {
            'created_at': '2023-10-31T12:00:00.000000',
            'updated_at': '2023-10-31T12:00:00.000000',
            'custom_attribute': '89'
        }
        base_model = BaseModel(**kwargs)
        self.assertEqual(base_model.created_at, datetime(2023, 10, 31, 12, 0))
        self.assertEqual(base_model.updated_at, datetime(2023, 10, 31, 12, 0))
        self.assertEqual(base_model.custom_attribute, '89')


if __name__ == '__main__':
    unittest.main()
