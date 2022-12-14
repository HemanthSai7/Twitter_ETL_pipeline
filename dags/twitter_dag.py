from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime

import tweepy
import pandas as pd
from datetime import datetime
import sys
from pprint import pprint

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




default_args = {
    'owner':'airflow',
    'depends_on_past':False,
    'start_date':datetime(2022,11,11),
    'email':['example@gmail.com'],
    'email_on_failure':False,
    'email_on_retry':False,
    'retries':1,
    'retry_delay':timedelta(minutes=1)
}

dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='Omdena Workshop'
)

run_job = PythonOperator(
    task_id='complete_twitter_etl',
    python_callable=run_etl,
    dag=dag
)

run_job