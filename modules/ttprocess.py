from modules.api import create_tweets_request_url, create_user_request_url, send_request


def get_hashtags(username, bearer_token):
    try:
        usr_url = create_user_request_url(username)
    except ValueError:
        return "Invalid username"

    found, id, err = get_user_id(usr_url, bearer_token)
    if not found:
        return err

    tweets_url = create_tweets_request_url(id)
    found, tweets, err = get_tweets(tweets_url, bearer_token)
    if not found:
        return err

    return search_hashtags(tweets)


def get_user_id(url, bearer_token):
    try:
        response = send_request(url, bearer_token)
        if "data" in response and "id" in response["data"]:
            return True, response["data"]["id"], ""
        return False, "", "User not found"
    except Exception as e:
        return False, "", e


def get_tweets(url, bearer_token):
    try:
        response = send_request(url, bearer_token)
        if has_tweets(response):
            return True, response["data"], ""
        return False, "", "Tweets not found"
    except Exception as e:
        return False, "", e


def has_tweets(data):
    return (
        "meta" in data
        and "result_count" in data["meta"]
        and data["meta"]["result_count"] > 0
    )


def search_hashtags(tweets):
    all_hashtags = []
    for tweet in tweets:
        hashtags = extract_hashtags(tweet["text"])
        all_hashtags += hashtags

    if len(all_hashtags) == 0:
        print("No hashtags found")
    return all_hashtags


def extract_hashtags(s):
    return set(part[1:].replace(".", "") for part in s.split() if part.startswith("#"))
