import tweepy
import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

# provide your access details below
access_token = "#####"
access_token_secret = "#####"
consumer_key = "#####"
consumer_secret = "#####"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Read your timeline of Twitter
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)