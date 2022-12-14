import os
import json
import tweepy
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

import pandas as pd


bearer = os.environ.get('BEARER')


# Twitter auth
client = tweepy.Client(bearer_token=bearer)

# Create the API object

res = client.search_recent_tweets(query="covid OR covid19 -is:retweet",
                                  tweet_fields=['created_at', 'lang'],
                                  expansions=['author_id']) # check fields for further refinement

users = {u['id']:u for u in res.includes['users']}

for t in res.data:
    if users[t.author_id]:
        user = users[t.author_id]
        print(t.id)
        print(user.username)




