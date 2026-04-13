from flask import current_app, render_template, request
from .models import reddit


@current_app.route("/")
def index():
    return render_template("index.html")


@current_app.post("/get_posts")
def get_posts():
    success = True
    msg = ""
    posts = []

    try:
        if request.json.get("subName"):
            posts = [
                {
                    "title": i.title,
                    "score": i.score,
                    "created_utc": i.created_utc,
                    "num_comments": i.num_comments,
                    "subName": i.subreddit.display_name,
                    "url": i.url,
                }
                for i in reddit.subreddit(request.json.get("subName")).hot()
            ]
        else:
            posts = [
                {
                    "title": i.title,
                    "score": i.score,
                    "created_utc": i.created_utc,
                    "num_comments": i.num_comments,
                    "subName": i.subreddit.display_name,
                    "url": i.url,
                }
                for i in reddit.front.hot()
            ]

    except Exception as e:
        success = False
        msg = str(e)

    return {"success": success, "msg": msg, "posts": posts}


@current_app.post("/get_subs")
def get_subs():
    success = True
    msg = ""
    subs = []

    try:
        subs = [i.display_name for i in reddit.user.subreddits(limit=None)]
    except Exception as e:
        success = False
        msg = str(e)

    return {"success": success, "msg": msg, "subs": subs}
