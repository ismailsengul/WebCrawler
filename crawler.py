import praw
import csv
from better_profanity import profanity
from tqdm import tqdm


reddit = praw.Reddit(
    client_id='CLIENT_ID',
    client_secret='CLIENT_SECRET',
    password='PASSWORD',
    user_agent='USER_AGENT',
    username='USERNAME',
)

subreddit = reddit.subreddit("technology")

total_posts = 100
top_posts = subreddit.top(time_filter='year', limit=total_posts)

with open('reddit_technology_posts.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Score', 'URL', 'Top Comment','Top Comment Author','Top Comment Score','Comment Authors'])

    for post in tqdm(top_posts, total=total_posts, desc="Collecting Data",colour='green'):
        top_comment = ""
        top_comment_score = float('-inf')
        post_title = post.title
        comment_authors = []
        for comment in post.comments:
            if isinstance(comment, praw.models.Comment):
                if comment.author:
                    comment_authors.append(comment.author.name)
                if comment.score > top_comment_score:
                    top_comment_score = comment.score
                    top_comment = comment.body
                    top_comment_author = comment.author

        if profanity.contains_profanity(top_comment):
            top_comment = "Warning : comment containing profanity!"
        if profanity.contains_profanity(post_title):
            post_title = "Warning : comment containing profanity!"

        writer.writerow([post_title, post.score, post.url, top_comment,top_comment_author,top_comment_score,comment_authors])

    