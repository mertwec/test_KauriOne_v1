import unittest
from unittest.mock import Mock, MagicMock, patch
from api_to_json import get_api_as_json
from requests.exceptions import Timeout


class TestApiToJson(unittest.TestCase):	
	@patch('api_to_json.get_api')
	def test_get_api(self, mock_get_api):
		mock_status_200 = Mock(status_code=200)		
		mock_status_200.json.return_value = {'name': 'Valentin',
											'age': 30,
											'married': True,
											'skils': ['Python3', 'Flask']}							
		mock_get_api.return_value = mock_status_200
		resp = get_api_as_json("http://localhost:5050/api_local")
		self.assertIsInstance(resp,  str)
		self.assertTrue(resp)
		self.assertEqual(resp, '{"name": "Valentin", "age": 30, "married": true, "skils": ["Python3", "Flask"]}')


	@patch('api_to_json.get_api')
	def test_not_get_api(self, mock_get_apierr):
		mock_get_apierr = Mock()
		mock_get_apierr.side_effect = Timeout("I'm tired of waiting")
		self.assertRaises(Exception, get_api_as_json, "http://localhost:5050/api_local",
		 	msg='blya')

if __name__ == '__main__':
	unittest.main()
