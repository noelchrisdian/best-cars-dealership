# Uncomment the imports below before you add the function code
# import requests
import os

import requests
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv("backend_url", default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    "sentiment_analyzer_url", default="http://localhost:5050/"
)


def get_request(endpoint, **kwargs):
    params = ""

    if kwargs:
        for key, value in kwargs.items():
            params = f"{params}{key}={value}&"

    request_url = f"{backend_url}{endpoint}"
    if params:
        request_url += f"?{params}"
    print(f"GET from {request_url}")

    try:
        response = requests.get(request_url)
        print(f"📡 Status Code: {response.status_code}")
        print(f"📦 Response JSON: {response.text}")
        return response.json()
    except BaseException:
        print("Network exception occured")


def analyze_review_sentiments(text):
    request_url = f"{sentiment_analyzer_url}analyze/{text}"

    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as error:
        print(f"Unexpected {error=}, {type(error)=}")
        print("Network exception occurred")


def post_review(data_dict):
    request_url = f"{backend_url}/insert_review"

    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except BaseException:
        print("Network exception occurred")
