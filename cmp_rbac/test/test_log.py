import unittest
import magic_manager
import flask
from unittest import mock

class UnitLog(unittest.TestCase):
    def test_do_logged(self):
        pass
    @mock.patch('flask.request')
    def test_log(self,mock_request):
        mock_request.headers.getlist.return_value = ['12']
        actual = magic_manager.log.logged(func=self.test_do_logged)
        print(actual())
        self.assertEqual(actual.__name__, 'test_do_logged')
