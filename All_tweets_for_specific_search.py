import tweepy
import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

# provide your access details below
access_token = "##########"
access_token_secret = "##########"
consumer_key = "##########"
consumer_secret = "##########"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


class listener(StreamListener):
    def on_data(self, raw_data):
        print(raw_data)
        return True
    def on_error(self, status_code):
        print(status_code)

twitterStream = Stream(auth, listener())
twitterStream.filter(track="cars")




