import tweepy
import pandas as pd
import json
from datetime import datetime

def run_etl():

    bearer = "Your bearer here :) "


    client = tweepy.Client(bearer_token=bearer)
    query = 'harcelement OR violence -is:retweet'

    tweets = client.search_recent_tweets(query=query,
                                         expansions=['author_id'],
                                         tweet_fields=['created_at', 'lang'],
                                         max_results=100)

    tweet_list = []
    users = {u['id']:u for u in tweets.includes['users']}

    for tweet in tweets.data:
        if users[tweet.author_id]:
            user = users[tweet.author_id]
            text = tweet['text']

            refined_tweet = {"user_id":user['id'],
                             "user_name":user['name'],
                             "text":text}

            tweet_list.append(refined_tweet)

    df = pd.DataFrame(tweet_list)
    df.to_csv("s3://airflow-omdena/harcelement.csv")

