import unittest
from magic_manager.models.user import UserDB

class TestUser(unittest.TestCase):

    def test_repr(self):
        db = UserDB()
        UserDB.__repr__(db)
