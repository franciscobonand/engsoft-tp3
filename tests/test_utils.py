import pytest
from modules.api import create_tweets_request_url, create_user_request_url
from modules.ttprocess import has_tweets, search_hashtags


@pytest.fixture
def user_url():
    return "https://api.twitter.com/2/users/by/username/test"


@pytest.fixture
def tweets_url():
    return "https://api.twitter.com/2/users/12345/tweets?max_results=50"


@pytest.fixture
def example_response_with_tweet():
    return {
        "data": [
            {
                "id": "1537503380368723970",
                "text": "⏱Data delivery, faster.\n\nToday, we reduced the latency for all v2 streaming endpoints by half, which includes the filtered and sampled stream endpoints.",
            }
        ],
        "meta": {
            "result_count": 1,
            "newest_id": "1537503380368723970",
            "oldest_id": "1522642323535847424",
            "next_token": "7140dibdnow9c7btw421dyz6jism75z99gyxd8egarsc4",
        },
    }


@pytest.fixture
def example_response_without_tweet():
    return {
        "data": [],
        "meta": {
            "result_count": 0,
            "newest_id": "1537503380368723970",
            "oldest_id": "1522642323535847424",
            "next_token": "7140dibdnow9c7btw421dyz6jism75z99gyxd8egarsc4",
        },
    }


def test_valid_username(user_url):
    url = create_user_request_url("test")
    assert url == user_url


def test_invalid_username():
    pytest.raises(ValueError, create_user_request_url, "test*")


def test_tweets_url(tweets_url):
    url = create_tweets_request_url("12345")
    assert url == tweets_url


def test_response_has_tweets(example_response_with_tweet):
    assert has_tweets(example_response_with_tweet)


def test_response_has_no_tweets(example_response_without_tweet):
    assert not has_tweets(example_response_without_tweet)


def test_tweet_has_no_hashtags():
    tweets = [{"text": "Nothing to see here, move along."}]
    assert search_hashtags(tweets) == "No hashtags found"


def test_tweet_has_hashtag():
    tweets = [{"text": "Nothing to see here, #move along."}]
    assert search_hashtags(tweets) == ["move"]


def test_tweet_has_multiple_hashtags():
    tweets = [{"text": "Nothing #to see #here, #move along."}]
    resp = search_hashtags(tweets)
    for item in ["to", "here", "move"]:
        assert item in resp


def test_multiple_tweets_with_hashtags():
    tweets = [
        {"text": "Nothing #to see here, move along."},
        {"text": "Nothing to see here, move along."},
        {"text": "Nothing to see #here, move along."},
        {"text": "Nothing to see here, #move along."},
    ]
    resp = search_hashtags(tweets)
    for item in ["to", "here", "move"]:
        assert item in resp


def test_multiple_tweets_without_hashtags():
    tweets = [
        {"text": "Nothing to see here, move along."},
        {"text": "Nothing to see here, move along."},
        {"text": "Nothing to see here, move along."},
        {"text": "Nothing to see here, move along."},
    ]
    assert search_hashtags(tweets) == "No hashtags found"


def test_joined_hashtags():
    tweets = [{"text": "Nothing #to#see#here, move along."}]
    assert search_hashtags(tweets) == ["to#see#here"]
