import os
import re
from os.path import dirname, join

import requests
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

bearer_token = os.environ.get("TT_BEARER")


def create_user_request_url(username):
    if re.match(r"/^[A-Za-z0-9_]{4,15}$/", username) != None:
        url = f"https://api.twitter.com/2/users/by/username/{username}"
        return url

    raise ValueError


def create_tweets_request_url(user_id):
    url = f"https://api.twitter.com/2/users/{user_id}/tweets?max_results=15"
    return url


def send_request(url):
    response = requests.request(
        "GET",
        url,
        headers={
            "User-Agent": "v2UserLookupPython",
            "Authorization": f"Bearer {bearer_token}",
        },
    )

    if response.status_code != 200:
        raise Exception(
            f"Request returned an error: {response.status_code} {response.text}"
        )
    return response.json()
