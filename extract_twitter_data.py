
#Write your search filter tweets in JSON file.

import tweepy
import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
#provide your access details below 
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

# Reads twitter feeds based on the key word
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('C:\\Users\\Prathamesh\\PycharmProjects\\DataSciencePython-master\\Twitter-Data-Analysis\\python.json', 'a') as f:  #change location here
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())

#change the keyword here
twitter_stream.filter(track=['#cricket'])
