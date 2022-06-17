import os

import pytest
from modules.api import create_user_request_url, send_request

# @pytest.fixture
# def bearer():
#     return os.environ.get("TT_BEARER")


# def test_valid_request(bearer):
#     url = create_user_request_url("TwitterDev")
#     resp = send_request(url, bearer)
#     assert resp["data"]["username"] == "TwitterDev"
