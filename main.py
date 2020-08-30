from teletweet.tweetapi import trending
from teletweet.telebot import telegram_bot_sendtext
import schedule
import time
from logger import logger


def ping():
    logger.info("Ping!")


def handler():
    trends = trending()
    logger.info("Get trends success")
    telegram_bot_sendtext(trends)
    logger.info("Message sent")


def main():
    handler()
    schedule.every(30).seconds.do(ping)
    schedule.every(60).minutes.do(handler)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
