import tweepy
import json
from teletweet import config


def trending():
    api_key = config.API_KEY
    api_secret_key = config.API_SECRET_KEY
    access_token = config.ACCESS_TOKEN
    access_token_secret = config.ACCESS_TOKEN_SECRET

    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    indonesian_woe_id = 1030077

    indonesian_trends = api.trends_place(indonesian_woe_id)

    trends = json.loads(json.dumps(indonesian_trends, indent=1))

    # clean_trends = []
    # for x in trends[0]["trends"]:
    #     if x["promoted_content"] is None:
    #         clean_trends.append({"name": x["name"], "volume": x["tweet_volume"]})

    return trends[0]["trends"]
