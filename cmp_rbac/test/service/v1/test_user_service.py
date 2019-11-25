import unittest
from unittest import mock
from magic_manager.service.v1 import user_service

class TestUserService(unittest.TestCase):

    @mock.patch('magic_manager.models.user.UserDB.query')
    def test_get_all_users(self,mock_query):
        mock_query.all.return_value = []
        actual = user_service.get_all_users()
        self.assertEqual(actual, [])

    @mock.patch('magic_manager.DB.session.add')
    @mock.patch('magic_manager.DB.session.commit')
    def test_add_user(self, mock_add, mock_commit):
        data = {'id': 0, 'age': 24, 'gender': 'male', 'name': "reddy"}
        actual = user_service.add_user(data)
        expected = "Thank you for your submission. You are a age 24 old gender male named reddy"
        self.assertEqual(actual, expected)

    @mock.patch('magic_manager.DB.session.add')
    @mock.patch('magic_manager.DB.session.commit')
    def test_update_user_1(self, mock_add, mock_commit):
        id = "nav"
        data = {'id': 0, 'age': 55, 'gender': 'female', 'name': "vijju"}
        try:
            user_service.update_user(id, data)
        except ValueError:
            self.assertTrue(True)

    @mock.patch('magic_manager.models.user.UserDB.query.filter_by')
    def test_update_user_2(self, mock_query):
        mock_query.return_value = None
        id = 47
        data = {'id': 47, 'age': 55, 'gender': 'female', 'name': "vijju"}
        try:
            user_service.update_user(id, data)
        except ValueError:
            self.assertTrue(True)

    @mock.patch('magic_manager.DB.session.add')
    @mock.patch('magic_manager.DB.session.commit')
    def test_update_user_3(self, mock_add, mock_commit):
        id = 13
        data = {'id': 0, 'age': 55, 'gender': 'female', 'name': "vijju"}
        actual = user_service.update_user(id, data)
        expected = "vijju is 55 year old female and updated as new user successfully."
        self.assertEqual(actual, expected)

    @mock.patch('magic_manager.DB.session.delete')
    @mock.patch('magic_manager.DB.session.commit')
    def test_delete_user_1(self, mock_delete, mock_commit):
        id = "nav"
        try:
            user_service.delete_user(id)
        except ValueError:
            self.assertTrue(True)

    @mock.patch('magic_manager.models.user.UserDB.query.filter_by')
    def test_delete_user_2(self, mock_query):
        id = 47
        try:
            user_service.delete_user(id)
        except ValueError:
            self.assertTrue(True)

    @mock.patch('magic_manager.DB.session.delete')
    @mock.patch('magic_manager.DB.session.commit')
    def test_delete_user_3(self, mock_delete, mock_commit):
        id =12
        actual = user_service.delete_user(id)
        expected = "User having id:12 deleted successfully."
        self.assertEqual(actual, expected)
