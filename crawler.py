import praw
import csv

reddit = praw.Reddit(
    client_id='CLIENT_ID',
    client_secret='CLIENT_SECRET',
    password='PASSWORD',
    user_agent='USER_AGENT',
    username='USERNAME',
)

subreddit = reddit.subreddit("python")

for post in subreddit.hot(limit=10):
    print(post.title)
     # Open (or create) a file to write to
    with open('reddit_posts.csv', 'w', newline='', encoding='utf-8') as file:
         writer = csv.writer(file)
         # Write header row
         writer.writerow(['Title', 'Score', 'URL'])
         for post in subreddit.hot(limit=10):
             # Write data for each post
             writer.writerow([post.title, post.score, post.url])