import tweepy
import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

# provide your access details below
access_token = "######"
access_token_secret = "######"
consumer_key = "######"
consumer_secret = "######"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
data = api.get_user('YourHandle')
print("My Twitter Handle:" , data.screen_name)
ct = 0

for friend in data.friends():
    print (friend.screen_name)
    ct = ct + 1
