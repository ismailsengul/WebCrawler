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

total_posts = 50
top_posts = subreddit.top(time_filter='year', limit=total_posts)

with open('reddit_technology_posts.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Score', 'URL', 'Top Comment', 'Top Comment Likes', 'Top Comment Dislikes', 'Worst Comment', 'Worst Comment Likes', 'Worst Comment Dislikes'])

    for post in tqdm(top_posts, total=total_posts, desc="Collecting Data",colour='green'):

        top_comment = ""
        top_comment_likes = 0
        top_comment_dislikes = 0
        worst_comment = ""
        worst_comment_likes = 0
        worst_comment_dislikes = 0
        top_score = float('-inf')
        worst_score = float('inf')
        post_title = post.title

        for comment in post.comments:
            if isinstance(comment, praw.models.Comment):

                if comment.score > top_score:
                    top_score = comment.score
                    top_comment = comment.body
                    top_comment_likes = comment.ups
                    top_comment_dislikes = comment.downs
                if comment.score < worst_score:
                    worst_score = comment.score
                    worst_comment = comment.body
                    worst_comment_likes = comment.ups
                    worst_comment_dislikes = comment.downs

        if profanity.contains_profanity(worst_comment):
            worst_comment = "Warning : comment containing profanity!"
        if profanity.contains_profanity(top_comment):
            top_comment = "Warning : comment containing profanity!"
        if profanity.contains_profanity(post_title):
            post_title = "Warning : comment containing profanity!"

        writer.writerow([post_title, post.score, post.url, top_comment, top_comment_likes, top_comment_dislikes, worst_comment, worst_comment_likes, worst_comment_dislikes])

    