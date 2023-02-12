#!/usr/bin/python3
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_id_is_uuid(self):
        self.assertIsInstance(self.base_model.id, str)
        self.assertEqual(len(self.base_model.id), 36)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_created_at_is_updated(self):
        old_created_at = self.base_model.created_at
        self.base_model.save()
        self.assertEqual(old_created_at, self.base_model.created_at)

    def test_updated_at_is_updated(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertGreater(self.base_model.updated_at, old_updated_at)

    def test_to_dict_contains_correct_keys(self):
        dct = self.base_model.to_dict()
        self.assertIn("id", dct)
        self.assertIn("created_at", dct)
        self.assertIn("updated_at", dct)
        self.assertIn("__class__", dct)

    def test_to_dict_values_are_correct(self):
        dct = self.base_model.to_dict()
        self.assertEqual(dct["id"], self.base_model.id)
        self.assertEqual(dct["created_at"], self.base_model.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(dct["updated_at"], self.base_model.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(dct["__class__"], "BaseModel")

    def test_str_representation(self):
        string_representation = str(self.base_model)
        self.assertIn(self.base_model.__class__.__name__, string_representation)
        self.assertIn(self.base_model.id, string_representation)
        self.assertIn(str(self.base_model.__dict__), string_representation)

if __name__ == '__main__':
    unittest.main()

