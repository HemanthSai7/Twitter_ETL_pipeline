import os
import json
import tweepy
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

bearer = os.environ.get('BEARER')

# Twitter auth
client = tweepy.Client(bearer_token=bearer)

# Create the Query object
query = 'harcelement -is:retweet'

#### GET MORE THAN 100 TWEETS
file_name = 'tweets.txt'

with open(file_name, 'a+') as f:

    for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=100).flatten(limit=500):
        #f.write('%s\n' % tweet.id)
        print(tweet)

