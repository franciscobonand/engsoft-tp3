import os

import pytest
from modules.api import create_user_request_url, send_request
from modules.ttprocess import get_hashtags

bearer_token = os.environ.get("TT_BEARER")


def test_valid_request():
    url = create_user_request_url("TwitterDev")
    resp = send_request(url, bearer_token)
    assert resp["data"]["username"] == "TwitterDev"
