from app import flask_app
import unittest

class FlaskRouteTests(unittest.TestCase):

    def setUp(self):
        self.app = flask_app.test_client()
        self.app.testing = True

    def test_invalid_request_method(self):
        response = self.app.post("/api/data")
        self.assertEqual(response.status_code, 405)
