import os


API_KEY = os.getenv("API_KEY", "Somesecret")
API_SECRET_KEY = os.getenv("API_SECRET_KEY", "somekeey")

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", "sometoken")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET", "rahasia")

BOT_TOKEN = os.getenv("BOT_TOKEN", "bottoken")
BOT_CHAT_ID = os.getenv("BOT_CHAT_ID", "chatid")
BOT_CHAT_ID_USER_TWEET = os.getenv("BOT_CHAT_ID_USER_TWEET", "user_chat_id")
