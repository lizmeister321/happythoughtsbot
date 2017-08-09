import tweepy
import json
import flickrapi
import random
import urllib


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

breaking_tweets = api.user_timeline('cnnbrk')
#for tweet in breaking_tweets:

#check for new tweet

#if new tweet:

	#find random baby animal on Flickr
api_key = config['flickr_api']['key']
api_secret = config['flickr_api']['secret']
flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')

animals = config['animals']

#gotta mix the cute animals up
pick_one = random.randrange(0, len(animals))
random_animal = "baby " + animals[pick_one]
print random_animal
search_results = flickr.photos.search(text=random_animal, license=(1,2,3,4,5,6,7), sort='relevance', safe_search=1, per_page=20 , page=1)
url = 
	#store pic
	#attach to tweet



