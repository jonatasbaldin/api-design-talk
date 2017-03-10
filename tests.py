import unittest
import requests


class RestfulAPITest(unittest.TestCase):
    def setUp(self):
        self.API_VERSION = 'v1'
        self.API_URL = 'http://private-53a56-pyzzausers.apiary-mock.com/api/{}'.format(
            self.API_VERSION
        )

    def test_get_user_list(self):
        response = requests.get('{url}/users/'.format(url=self.API_URL))
        data = response.json()

        test_data = {
            'pagination': {
                'page_size': 20,
                'count': 1,
                'next': '/api/v1/<section>/?page=2',
                'current': 1,
                'previous': 'null'
            },
            'data': [
                {
                    'id': 'd9b43773-c41c-4854-8e84-d0cd09365022',
                    'name': 'Jonatas Baldin',
                    'username': '@jonatasbaldin',
                    'bio': 'Lazzy to write a bio :('
                }
            ],
            'links': [
                {
                    'rel': 'self',
                    'uri': '/api/v1/users/'
                }
            ]
        }

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, test_data)

    def test_get_user_detail(self):
        response = requests.get('{url}/users/jonatasbaldin/'.format(url=self.API_URL))
        data = response.json()

        test_data = {
            'pagination': '',
            'data': {
                'id': 'd9b43773-c41c-4854-8e84-d0cd09365022',
                'name': 'Jonatas Baldin',
                'username': '@jonatasbaldin',
                'bio': 'Lazzy to write a bio :('
            },
            'links': [
                {
                    'rel': 'self',
                    'uri': '/api/v1/users/jonatasbaldin/'
                },
                {
                    'rel': 'followers',
                    'uri': '/api/v1/users/jonatasbaldin/followers/'
                }
            ]
        }

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, test_data)

    def test_post_user(self):
        post_data = {
            'name': 'Jonatas Baldin',
            'username': '@jonatasbaldin',
            'bio': 'Lazzy to write a bio :('
        }

        response = requests.post(
            '{url}/users/'.format(url=self.API_URL),
            data=post_data
        )
        data = response.json()

        test_data = {
            'pagination': '',
            'data': {
                'id': 'd9b43773-c41c-4854-8e84-d0cd09365022',
                'name': 'Jonatas Baldin',
                'username': '@jonatasbaldin',
                'bio': 'Lazzy to write a bio :('
            },
            'links': [
                {
                    'rel': 'self',
                    'uri': '/api/v1/users/jonatasbaldin/'
                },
                {
                    'rel': 'followers',
                    'uri': '/api/v1/users/jonatasbaldin/followers/'
                }
            ]
        }

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data, test_data)

    def test_patch_user(self):
        patch_data = {
            'name': 'Jonatas Baldin',
            'username': '@jonatasbaldin',
            'bio': 'Lazzy to write a bio :('
        }

        response = requests.patch(
            '{url}/users/jonatasbaldin/'.format(url=self.API_URL),
            data=patch_data
        )
        data = response.json()

        test_data = {
            'pagination': '',
            'data': {
                'id': 'd9b43773-c41c-4854-8e84-d0cd09365022',
                'name': 'Jonatas Baldin',
                'username': '@jonatasbaldin',
                'bio': 'Lazzy to write a bio :('
            },
            'links': [
                {
                    'rel': 'self',
                    'uri': '/api/v1/users/jonatasbaldin/'
                },
                {
                    'rel': 'followers',
                    'uri': '/api/v1/users/jonatasbaldin/followers/'
                }
            ]
        }

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, test_data)

    def test_delete_user(self):
        response = requests.delete(
            '{url}/users/jonatasbaldin/'.format(url=self.API_URL),
        )
        self.assertEqual(response.status_code, 204)


if __name__ == '__main__':
    unittest.main()
