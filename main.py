import os
from os.path import dirname, join

from dotenv import load_dotenv

from modules.ttprocess import get_hashtags

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

bearer_token = os.environ.get("TT_BEARER")


if __name__ == "__main__":
    username = input("enter username: ")
    result = get_hashtags(username, bearer_token)
    print(result)
