import requests
import json


def get_api(url_api):
	try:
		return requests.get(url_api)
	except requests.exceptions.ConnectionError as ce:
		return f"url {url_api} not exist, run server", ce


def get_api_as_json(url_api):
	response = get_api(url_api)
	if response.status_code == 200:
		return json.dumps(response.json())
	return f'Can`t get api on url: {url_api}'


if __name__ == "__main__":
	api_cat = "https://catfact.ninja/fact"
	cat = get_api_as_json(api_cat)
	print(type(cat), cat)
