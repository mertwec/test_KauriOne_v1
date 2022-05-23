import unittest
import json
from api_to_json import get_api_as_json, get_api


class TestApiToJson(unittest.TestCase):
	def setUp(self):
		self.api_err = "https://catfact.ninja/error"
		self.api_local = "http://localhost:5050/api_local"

	def test_not_get_api(self):
		self.assertEqual(get_api_as_json(self.api_err), 
			f'Can`t get api on url: {self.api_err}')

	def test_get_json_api(self):
		self.assertEqual(json.loads(get_api_as_json(self.api_local)),
						{'name': 'Valentin',
	                    'email': 'val.work@example.com',
	                    'age': 30,
	                    'married': True,
	                    'skils': ['Python3', 'Flask', 'json'],
	                    'some': None}
						)


class TestGetApi(unittest.TestCase):
	def setUp(self):
		self.api_err = "https://catfact.ninja/error"
		self.api_local = "http://localhost:5050/api_local"

	def test_get_response(self):
		self.assertEqual(str(get_api(self.api_local)), '<Response [200]>')
	
	def test_not_get_responce(self):
		self.assertFalse(isinstance(get_api(self.api_err), tuple))


if __name__ == '__main__':
	unittest.main()
