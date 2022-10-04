import json

from flask import current_app, render_template, request

from reddit_front_page.models import Post, reddit


@current_app.route("/")
def index():
    subs = list(reddit.user.subreddits())
    return render_template("index.html", subs=subs)


@current_app.route("/get_posts")
def get_posts():
    return dict(
        posts=[
            Post(i.id).to_dict
            for i in reddit.subreddit(request.args.get("display_name")).hot(limit=25)
        ]
    )
