import unittest
from main import db, api, FERNET_KEY, app
from flask_restful import Api, Resource
from flask import Flask, jsonify, request, Response

class FlaskTestCase(unittest.TestCase):
    #check if status code is 200 or not
    def test_index(self):
        tester=app.test_client(self)
        response=tester.get('/v1/api/demo')
        code=response.status_code
        self.assertEqual(code, 200)

    #check if application content is json or not
    def test_index_route(self):
        tester=app.test_client(self)
        response=tester.get('/v1/api/demo')
        self.assertEqual(response.content_type, "application/json")

    #check if value returned is equal to the given value or not
    def test_index_data(self):
        tester=app.test_client(self)
        response=tester.get('/v1/api/demo')
        self.assertEqual(b'Test' in response.data)

if __name__ == '__main__':
    unittest.main()