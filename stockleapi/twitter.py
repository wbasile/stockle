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
    # GET arguments: list of keywords to search
    data = {'lang':'en', 'q':keyword ,'count':config.tweet_list_size}
    response = requests.get(config.url_twitter, params=data, auth=auth, stream=True)
    results = response.json()
    try:
        tweets = results['statuses']
    except:
        log.error('cannot retrieve tweets')
        tweets = []
    return tweets

def get_tweets(keyword):
    raw_tweets = get_keywords_stream(keyword)
    tweets = []
    for tweet in raw_tweets:
        tweets.append({'id':tweet['id'], 'text':tweet['text']})
    return {'tweets':tweets}

'''
def get_items(keyword):
    tweets = get_tweets(keyword)
    items = {'items':[]}
    for tweet in tweets['tweets']:
        try:
            response = alchemy.sentiment_targeted('text', tweet['text'], keyword)
            sentiment = response['docSentiment']['type']
            if sentiment == 'positive' or sentiment == 'negative':
                sentiment_score = eval(response['docSentiment']['score'])
            else:
                sentiment_score = 0.0
            items['items'].append({'id' : str(tweet['id']),
                                   'text' : tweet['text'],
                                   'sentiment' : sentiment_score})
        except:
            pass
    return items

'''

def get_items(query):
    return {'items':[
             {'text': u"my headphone jack isn't working anymore what kind of apple sorcery is this",
              'id': '776471755049226240',
              'sentiment': -0.575447},
             {'text': u'Apple shares jump 2% again ahead of iPhone 7 sales https://t.co/u8OFrrMDOs #Tips2Trade #T2T https://t.co/L7mblr95FV',
              'id': '776471754399068160',
              'sentiment': 0.0},
             {'text': u'Neoliberalism: \u2018Profit Goes To Apple And Microsoft, Not To The Taxpayer\u2019 \u2013 By Kit\xa0O\u2019Connell https://t.co/iaZ0adCw9I https://t.co/hetR4jb0QC',
              'id': '776471749948944384',
              'sentiment': -0.321275}]}

    return items
