import praw

from reddit_dash import config

reddit = praw.Reddit(
    client_id=config.CLIENT_ID,
    user_agent=config.USER_AGENT,
    client_secret=config.CLIENT_SECRET,
    username=config.USERNAME,
    password=config.PASSWORD,
)
