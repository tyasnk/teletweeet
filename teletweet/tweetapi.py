import time
from datetime import datetime, timedelta
from typing import List

from tweepy import Cursor

from logger import logger
import tweepy
import json
from teletweet import config


class TweetHandler:
    def __init__(self):
        pass

    def api(self):
        api_key = config.API_KEY
        api_secret_key = config.API_SECRET_KEY
        access_token = config.ACCESS_TOKEN
        access_token_secret = config.ACCESS_TOKEN_SECRET

        auth = tweepy.OAuthHandler(api_key, api_secret_key)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        return api

    def trending(self):
        api = self.api()
        indonesian_woe_id = 1030077

        indonesian_trends = api.trends_place(indonesian_woe_id)

        trends = json.loads(json.dumps(indonesian_trends, indent=1))

        # clean_trends = []
        # for x in trends[0]["trends"]:
        #     if x["promoted_content"] is None:
        #         clean_trends.append({"name": x["name"], "volume": x["tweet_volume"]})

        return trends[0]["trends"]

    def followed_user_tweet(self, user_ids: List[str]):
        api = self.api()
        if not user_ids:
            logger.warning("User ids must be specified")
            return

        tweets = []
        tweet_count = 0

        page = 1
        raw_url = "https://twitter.com/{}/status/{}"
        since = datetime.utcnow() - timedelta(hours=1)

        for user_id in user_ids:
            logger.info("getting tweets from: {}".format(user_id))
            try:
                for status in Cursor(api.user_timeline, page=page, id=user_id).items(20):
                    if status.created_at <= since:
                        continue
                    else:
                        tweet_count += 1
                        if status.retweeted or status.favorited:
                            continue
                        if hasattr(status, "retweeted_status"):
                            continue
                        if status.retweet_count > 20 or status.favorite_count > 20:
                            url = raw_url.format(status.user.screen_name, status.id)
                            tweets.append(url)
            except Exception as e:
                logger.warning("User Id: {} {}".format(user_id, e))
                pass

        return tweets
