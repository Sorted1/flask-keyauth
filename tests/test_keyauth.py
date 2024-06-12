import unittest
from flask import Flask, session
from flask_keyauth import KeyAuthAPI

class TestKeyAuthAPI(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.secret_key = 'test_secret_key'
        self.client = self.app.test_client()
        self.api = KeyAuthAPI('test_name', '1234567890')

    def test_init_invalid_credentials(self):
        with self.app.app_context():
            result = self.api.init()
            self.assertTrue('Go to' in result)

if __name__ == '__main__':
    unittest.main()