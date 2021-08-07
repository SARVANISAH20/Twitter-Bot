from re import search
import tweepy
import time

consumer_key = "BPdJfCYCyu13G1Bm7kmoUj0rc"
consumer_secret = "zZZbrbAP5SePR3QQu3IhtLgY8I5kBkpBGSfCxtncukx6bAwrjm"
key = "1401512364634222598-dre2NIQNpYd0c90WjZPycDb4BAAPZg"
secret = "wVCqCAnnYvwOWn8G5IjWDUT57OThivuM6zpY4MgygRczA"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

hashtag = "pythonlearning"
tweetNumber = 3
tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def searchbot():

    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Done!")
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(5)
searchbot()
