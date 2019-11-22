import praw
import csv
import sys

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='',
                     username='',
                     password='')

results = []

def viewPosts(sub):
  for submission in reddit.subreddit(sub).hot(limit=25):
    current = [submission.title[:75],
               submission.subreddit.display_name,
               submission.url,
               submission.id,
               submission.subreddit.display_name,
               submission.created_utc
              ]
    results.append(current)
    
  with open("hotPosts.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(results)
      
viewPosts(sys.argv[1])