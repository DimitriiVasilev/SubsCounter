import unittest
from unittest.mock import patch

from apihelper import CommunityAPI, AuthorizationError


class TestAPI(unittest.TestCase):

    def test_raises_AuthorizationError_with_wrong_token(self):
        api = CommunityAPI('wrong_token')
        with self.assertRaises(AuthorizationError):
            api.get_subs_count(1)

    @patch('apihelper.requests')
    def test_ValueError_shows_response(self, mock_requests):
        mock_requests.get().text = 'Response'
        mock_requests.get().json.side_effect = ValueError

        api = CommunityAPI('token')
        try:
            api.get_subs_count(1)
        except ValueError as e:
            self.assertIn('Response', e.args)
