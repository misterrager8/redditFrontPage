import os

import dotenv

dotenv.load_dotenv()

ENV = os.getenv("env")
DEBUG = os.getenv("debug").lower() == "true"

# PRAW config
CLIENT_ID = os.getenv("client_id")
USER_AGENT = os.getenv("user_agent")
CLIENT_SECRET = os.getenv("client_secret")
USERNAME = os.getenv("username")
PASSWORD = os.getenv("password")
