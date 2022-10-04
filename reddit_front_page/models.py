import datetime

import praw

from reddit_front_page import config

reddit = praw.Reddit(
    client_id=config.CLIENT_ID,
    user_agent=config.USER_AGENT,
    client_secret=config.CLIENT_SECRET,
    username=config.USERNAME,
    password=config.PASSWORD,
)


class Post(object):
    def __init__(self, id: str):
        self.id = id
        self.submission = reddit.submission(self.id)

    @property
    def created_utc(self):
        return datetime.datetime.utcfromtimestamp(self.submission.created_utc).strftime(
            "%b %-d %-I:%M %p"
        )

    @property
    def to_dict(self):
        return dict(
            title=self.submission.title,
            score=self.submission.score,
            created_utc=self.created_utc,
            num_comments=self.submission.num_comments,
            url=self.submission.url,
        )
