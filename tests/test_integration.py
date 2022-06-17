import os
from os.path import dirname, join

import pytest
from dotenv import load_dotenv
from modules.api import create_user_request_url, send_request
from modules.ttprocess import get_hashtags

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

bearer_token = os.environ.get("TT_BEARER")


def test_valid_request():
    url = create_user_request_url("TwitterDev")
    resp = send_request(url, bearer_token)
    assert resp["data"]["username"] == "TwitterDev"
