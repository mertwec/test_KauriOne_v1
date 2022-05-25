import requests
import json
from requests.exceptions import Timeout


def get_api(url_api):
	return requests.get(url_api, timeout=5)


def get_api_as_json(url_api):
	response = get_api(url_api)
	if response.status_code == 200:
		return json.dumps(response.json())
	raise Exception(f'Can`t get api on url: {url_api}')


if __name__ == "__main__":
	# api_loc = "http://localhost:5050/api_local"
	api_cat = "https://catfact.ninja/fact"
	cat = get_api_as_json(api_cat)
	print(type(cat), cat)
