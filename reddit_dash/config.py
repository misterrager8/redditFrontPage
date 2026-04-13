import os
import dotenv

dotenv.load_dotenv()

PORT = "7734"
# PRAW config
CLIENT_ID = os.getenv("client_id")
USER_AGENT = os.getenv("user_agent")
CLIENT_SECRET = os.getenv("client_secret")
USERNAME = os.getenv("username")
PASSWORD = os.getenv("password")
