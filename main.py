import requests
import praw

reddit = praw.Reddit(client_id='jXCPXiuviPOGHA', client_secret='WTxSVdlLC5ZjWXhBLvQ2qTkkhCk', username='livestreamstwitter', password='cookies', user_agent='linux:livestreamtwitter:v1.0 (by /u/sorieus')

subreddit = reddit.subreddit('livestreamfail')

top_livestreamfail = subreddit.top(time_filter='month' ,limit=25)

for submission in top_livestreamfail:
    if not submission.stickied:
        print(f'Title: {submission.title}\n\n Url:{submission.url}\n')