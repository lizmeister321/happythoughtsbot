import tweepy
import json
import flickrapi


#import keys
with open('config.json') as cfg:
	config = json.load(cfg)


consumer_key = config['twitter_api']['consumer_key']
consumer_secret = config['twitter_api']['consumer_secret']
access_token = config['twitter_api']['access_token']
access_token_secret = config['twitter_api']['access_token_secret']

#getting started with tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
pp = pprint.PrettyPrinter()

breaking_tweets = api.user_timeline('cnnbrk')
#for tweet in breaking_tweets:

#check for new tweet

#if new tweet:

	#find random baby animal on Flickr
	#store pic
	#attach to tweet



