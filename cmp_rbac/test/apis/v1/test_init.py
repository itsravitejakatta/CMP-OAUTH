import unittest
from magic_manager.apis import v1

class TestInit(unittest.TestCase):

    def test_handle_valueerror_exception(self):
        actual = v1.handle_valueerror_exception(error='false')
        self.assertEqual(actual[1], 400)

    def test_handle_general_exception(self):
        actual = v1.handle_general_exception(error='false')
        self.assertEqual(actual[1], 500)
