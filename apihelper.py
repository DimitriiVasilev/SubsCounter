import requests


class AuthorizationError(Exception):
    """raises when authorization failed"""


class CommunityAPI:
    """"Class for retrieving information from VK communities"""

    def __init__(self, access_token):
        """
        Takes access token as an argument.
        It's needed for authorization in VK
        """
        self.access_token = access_token

    def get_subs_count(self, community_id):
        """
        Retrieves number of subscribers in community.
        Raises ValueError if got not json response or there was no
        data about subscribers
        """
        params = {
            'access_token': self.access_token,
            'group_id': community_id,
            'count': 0,
            'v': 5.101
        }
        response = requests.get(
            'https://api.vk.com/method/groups.getMembers',
            params=params
        )
        if '"error_code":5' in response.text:
            raise AuthorizationError('Authorization failed with token:', self.access_token)
        try:
            return response.json()['response']['count']
        except (ValueError, KeyError):
            raise ValueError('Got bad response:', response.text)
