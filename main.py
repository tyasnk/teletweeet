from teletweet.tweetapi import TweetHandler
from teletweet.telebot import telegram_bot_send_trending, telegram_bot_send_user_tweets
import schedule
import time
from logger import logger


def ping():
    logger.info("Ping!")


def handler():
    tweet_handler = TweetHandler()
    trends = tweet_handler.trending()
    logger.info("Get trends success")
    telegram_bot_send_trending(trends)
    logger.info("Trending sent")
    tweets = tweet_handler.followed_user_tweet(
        user_ids=[
            "@AdibHidayat",
            "@felixdass",
            "@TrinityOptimaP",
            "@SonyMusicID",
            "@umusicindonesia",
            "@harlanboer",
            "@deathrockstar",
            "@KompasTravel",
            "@marischkaprue",
            "@TrinityTraveler",
            "@drhaltekehalte",
            "@thspcwndrr",
            "@wisatanesa",
            "@indtravel",
            "@BacpackerINA",
            "@BackpackerInfo",
            "@idbcpr",
            "@lostpacker",
            "@PergiDulu",
            "@IamMariza",
            "@BackpackSeru",
            "@wjournal",
            "@pophariini",
            "@gigsplay",
            "@NGIndonesia",
            "@GNFI",
            "@VICE_ID",
        ]
    )

    for url in tweets:
        telegram_bot_send_user_tweets(url=url)

    logger.info("User tweets sent")


def main():
    handler()
    schedule.every(10).minutes.do(ping)
    schedule.every(60).minutes.do(handler)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
