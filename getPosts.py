import praw
import csv

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='',
                     username='',
                     password='')

results = []

def viewPosts():
  for submission in reddit.front.hot(limit=50):
    current = [submission.title,
               submission.subreddit.display_name,
               submission.url,
               submission.id,
               submission.subreddit.display_name]
    results.append(current)
    
  with open("hotPosts.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(results)
      
viewPosts()