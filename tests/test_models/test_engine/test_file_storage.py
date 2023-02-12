#!/usr/bin/python3

import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_storage = FileStorage()
        self.base_model = BaseModel()

    def test_all(self):
        # Test that all method returns the correct dictionary
        self.file_storage.new(self.base_model)
        self.assertEqual(self.file_storage.all(), {'BaseModel.{}'.format(self.base_model.id): self.base_model})

    def test_save(self):
        # Test that save method correctly serializes the objects to the JSON file
        self.file_storage.new(self.base_model)
        self.file_storage.save()

        with open("file.json", "r") as file:
            data = json.load(file)

        self.assertEqual(data, {'BaseModel.{}'.format(self.base_model.id): self.base_model.to_dict()})

    def test_reload(self):
        # Test that reload method correctly deserializes the JSON file to objects
        self.file_storage.new(self.base_model)
        self.file_storage.save()
        self.file_storage.reload()

        self.assertEqual(self.file_storage.all(), {'BaseModel.{}'.format(self.base_model.id): self.base_model})

if __name__ == '__main__':
    unittest.main()

