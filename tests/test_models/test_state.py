#!/usr/bin/python3
""" doctest unittest """
import unittest
import pep8
from models.state import State
import os


class TestBase(unittest.TestCase):
    """ test """

    def test_pep8(self):
        """ test pep8 """
        style = pep8.StyleGuide(quiet=True)
        file_state = "models/state.py"
        file_test_state = "tests/test_models/test_state.py"
        check = style.check_files([file_state, file_test_state])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")

    @classmethod
    def setUpClass(cls):
        """ first set up
        check = style.check_files([file_state, file_test_state])
        """
        cls.ins = State()

    @classmethod
    def teardown(cls):
        """ final statement """
        del cls.ins
        try:
            os.remove("file.json")

    def test_Userdoc(self):
        """ test base model documentation
        self.assertNotEqual(len(models.__doc__), 0)
        self.assertNotEqual(len(models.base_model.__doc__), 0)

        """
        self.assertNotEqual(len(State.__doc__), 0)

    def test_BaseModelAttr(self):
        """ test basemodel attributes """
        self.assertEqual(hasattr(self.ins, "name"), True)

    def test_isinstance(self):
        self.assertTrue(isinstance(self.ins, State))


if __name__ == '__main__':
    unittest.main()
