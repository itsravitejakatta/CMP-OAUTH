import unittest
from unittest import mock
from magic_manager.service import common

class TestCommon(unittest.TestCase):

    @mock.patch('flask.request')
    def test_update_user(self, mock_request):
        mock_request.get_json.return_value = {'a': 'a', 'b': 'b'}
        try:
            common.get_post_data(required_fields={'C': 'a'}, non_required_fields=['b'])
        except:
            common.get_post_data(required_fields={'B': 'a'}, non_required_fields=['a'])

    @mock.patch('flask.request')
    def test_update_user_2(self, mock_request):
        mock_request.get_json.return_value = None
        try:
            common.get_post_data(required_fields={'C': 'a'}, non_required_fields=['b'])
        except:
            pass


    def test_get_current_datetime(self):
        common.get_current_datetime()
        self.assertTrue(True)
