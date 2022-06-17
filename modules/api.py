import re

import requests


def create_user_request_url(username):
    if re.match(r"^[A-Za-z0-9_]{4,15}$", username) != None:
        url = f"https://api.twitter.com/2/users/by/username/{username}"
        return url

    raise ValueError


def create_tweets_request_url(user_id):
    url = f"https://api.twitter.com/2/users/{user_id}/tweets?max_results=50"
    return url


def send_request(url, bearer_token):
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
