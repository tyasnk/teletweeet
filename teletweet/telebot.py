from datetime import datetime
import pytz
from telegram import Bot
from teletweet import config


def telegram_bot_send_trending(trending_data):
    bot_token = config.BOT_TOKEN
    bot_chat_id = config.BOT_CHAT_ID
    crawled_time = datetime.now(tz=pytz.timezone("Asia/Jakarta")).strftime(
        "%Y/%m/%d %H:%M:%S"
    )

    bot = Bot(token=bot_token)
    trends_format = "Twitter Trends\nCrawled At: {}\n\n".format(crawled_time)
    for trend in trending_data:
        tmp = "{}: {}\n".format(trend["name"], trend["tweet_volume"])
        trends_format += tmp
    bot.send_message(
        chat_id=bot_chat_id, text=trends_format
    )


def telegram_bot_send_user_tweets(url):
    bot_token = config.BOT_TOKEN
    bot_chat_id = config.BOT_CHAT_ID_USER_TWEET

    bot = Bot(token=bot_token)
    bot.send_message(
        chat_id=bot_chat_id, text=url
    )
