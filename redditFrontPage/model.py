import datetime


class Sub:
    def __init__(self,
                 name: str,
                 color: str):
        self.name = name
        self.color = color


class Post:
    def __init__(self,
                 title: str,
                 url: str,
                 time_posted: datetime.datetime):
        self.title = title
        self.url = url
        self.time_posted = time_posted


class User:
    def __init__(self,
                 username: str,
                 user_age: datetime.datetime):
        self.username = username
        self.user_age = user_age


class Comment:
    def __init__(self,
                 text: str,
                 username: str,
                 time_posted: datetime.datetime):
        self.text = text
        self.username = username
        self.time_posted = time_posted
