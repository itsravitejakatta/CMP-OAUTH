from magic_manager.apis.v1.users import UserView, UserUpdate
import unittest
from unittest import mock
import flask


class TestUsers(unittest.TestCase):

    @mock.patch('magic_manager.service.v1.user_service.get_all_users')
    def test_get(self,mock_user_service):
        mock_user_service.get_all_users.return_value = {}
        actual = UserView().get()
        self.assertEqual(actual[1], 200)

    @mock.patch('flask.request')
    @mock.patch('magic_manager.service.v1.user_service.add_user')
    def test_post(self, mock_flask, mock_user_service):
        mock_user_service.add_user.return_value = {}
        flask.request.json = {}
        actual = UserView().post()
        self.assertEqual(actual[1], 201)

    @mock.patch('flask.request')
    @mock.patch('magic_manager.service.v1.user_service.update_user')
    def test_put(self, mock_flask, mock_user_service):
        mock_user_service.update_user.return_value = {}
        flask.request.json = {}
        actual = UserUpdate().put(id)
        self.assertEqual(actual[1], 201)

    @mock.patch('magic_manager.service.v1.user_service.delete_user')
    def test_delete(self, mock_user_service):
        mock_user_service.delete_user.return_value = {}
        actual = UserUpdate().delete(id)
        self.assertEqual(actual[1], 200)
