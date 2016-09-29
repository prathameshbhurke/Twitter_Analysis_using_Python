# This code provides all your Twitter tweets

import tweepy
import time
import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

# provide your access details below
access_token = "########"
access_token_secret = "########"
consumer_key = "########"
consumer_secret = "########"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
def process_or_store(tweet):
    print(json.dumps(tweet))
for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)

