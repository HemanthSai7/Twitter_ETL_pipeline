import tweepy
import pandas as pd
import json
from datetime import datetime


bearer = "Your bearer here :) "

client = tweepy.Client(bearer_token=bearer)
query = 'harcelement -is:retweet'

###SEE HOW MANY TWEETS FOR A CERTAIN TOPIC (recent tweets count for the last 7 days)

counts = client.get_recent_tweets_count(query=query, granularity='day')

for count in counts.data:
    print(count)
