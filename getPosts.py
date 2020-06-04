import praw
import csv
import sys

reddit = praw.Reddit()

results = []

def hotPosts():
  for submission in reddit.front.hot(limit=50):
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
    
  del results[:]
    
def subPosts(sub):
  for submission in reddit.subreddit(sub).hot(limit=25):
    current = [submission.title[:75],
               submission.subreddit.display_name,
               submission.url,
               submission.id,
               submission.subreddit.display_name,
               submission.created_utc
              ]
    results.append(current)
    
  with open("subPosts.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(results)
    
  del results[:]

if __name__ == "__main__":
  if len(sys.argv) < 2:
    hotPosts()
  else:
    subPosts(sys.argv[1])