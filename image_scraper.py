import praw
import os
from urllib.request import urlretrieve
from datetime import datetime 

if not os.path.exists("naughty_pics"):
	os.mkdir("naughty_pics")
else:
	os.chdir("naughty_pics")

reddit = praw.Reddit(
    client_id="YOUR_ID",
    client_secret="YOUR_SECRET",
    user_agent="corinna-kopf-bot",
)

for post in reddit.subreddit("corinnakopfnsfws").hot(limit=None):
	if "jpg" in post.url:
		urlretrieve(post.url,f"{post.id}.jpg")
