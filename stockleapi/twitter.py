import requests
from requests_oauthlib import OAuth1
import json
import logging as log
from os.path import join, dirname
import config
from alchemy import AlchemyAPI
import random


# OAuth 1 authentication
auth = OAuth1(config.consumer_key,
              config.consumer_secret,
              config.oauth_token,
              config.oauth_secret)

# Create the AlchemyAPI Object
alchemy = AlchemyAPI()

def get_keywords_stream(keyword):
    # POST data: list of keywords to search
    data = {'lang':'en', 'q':keyword ,'count':config.tweet_list_size}
    response = requests.get(config.url_twitter, params=data, auth=auth, stream=True)
    results = response.json()
    tweets = results['statuses']
    return tweets

def get_tweets(keyword):
    tweets = get_keywords_stream(keyword)
    return [tweet['text'] for tweet in tweets]

def get_sentiment(keyword):
    tweets = get_tweets(keyword)
    sentiment_scores = []
    for tweet in tweets:
        try:
            response = alchemy.sentiment_targeted('text', tweet, keyword)
            sentiment = response['docSentiment']['type']
            if sentiment == 'positive' or sentiment == 'negative':
                sentiment_score = eval(response['docSentiment']['score'])
            else:
                sentiment_score = 0.0
            print "{0:.2f}\t{1}".format(sentiment_score, tweet)
            sentiment_scores.append(sentiment_score)
        except:
            pass
    return sentiment_scores



def get_items(query,n=10):
    item_list = []
    
    for i in range(n):
        item = {}
        item["title"] = "Tweet about "  + query + " " + str(i)
        item["link"] = "http://www.twitter.com/twitter_" + query + "_" + str(i)
        item["sentiment"] = random.random() * 2 - 1
        
        item_list += [item]
        
    return item_list
    
