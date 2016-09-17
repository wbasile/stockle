import requests
from requests_oauthlib import OAuth1
import json
import logging as log
from os.path import join, dirname
import config
import utils
import random

# OAuth 1 authentication
auth = OAuth1(config.consumer_key,
              config.consumer_secret,
              config.oauth_token,
              config.oauth_secret)

def get_keywords_stream(keyword):
    """ get tweets ('statuses') from the Twitter search API.
    API arguments: list of keywords to search, language
    """
    data = {'lang':'en', 'q':keyword}
    response = requests.get(config.url_twitter, params=data, auth=auth, stream=True)
    results = response.json()
    try:
        tweets = results['statuses']
    except:
        log.error('cannot retrieve tweets')
        tweets = []
    return tweets

def get_tweets(keyword):
    """ get only the ID and the text of the tweets to further process them
    with sentiment analysis.
    """
    raw_tweets = get_keywords_stream(keyword)
    tweets = []
    for tweet in raw_tweets:
        tweets.append({'id':tweet['id'], 'text':tweet['text']})
    return {'tweets':tweets}

'''
def get_items(keyword):
    """
    Access the Twitter API, search for the input keyword. For each tweet pass
    its text to the sentiment analysis API (AlchemyAPI).
    Returns a list of tweet IDs with a sentiment score.

    Input: a string containing the name of a company.
    Output: JSON containing a list of items (id, text, sentiment)
    """

    tweets = get_tweets(keyword)
    items = {'items':[]}
    for tweet in tweets['tweets']:
        sentiment_score = utils.get_sentiment(tweet['text'], 'text', 'targeted', keyword)
        if sentiment_score:
            items['items'].append({'id' : str(tweet['id']),
                                   'text' : tweet['text'],
                                   'sentiment' : sentiment_score})

        # stop cycling when reaching the desired item list size
        if len(items['items']) >= config.tweet_list_size:
            break
    return items
'''

# mock data
def get_items(query):
    return {'items': [
             {'text': u'Ibm 000-m75 take-home examination research and development fire engine: IfZ',
              'id': '777155426689224705',
              'sentiment': 0.460114},
             {'text': u'Grush captures data and sends them to the IBM #Cloud, where it is analyzed and turn into fun #games https://t.co/BJgjYYLz2u',
              'id': '777155409551429632',
              'sentiment': 0.634072},
             {'text': u'Great presentation from Fletcher @fletcherprevin regarding Mac@IBM, Switch to Macs from PCs. #JAMF https://t.co/8Pb4yK6kcC',
              'id': '777155371731390467',
              'sentiment': 0.558004},
             {'text': u'RT @AlexTarabrinIBM: #Datascientist should join the webcast on Sept. 22nd on IBM Data Science Experience #DSX https://t.co/H6JYinOaFS',
              'id': '777155312390381568',
              'sentiment': 0.264104},
             {'text': u'@SanjayVadia this IBM Watson seems to be the next big thing. Is there everywhere.',
              'id': '777155208489017345',
             'sentiment': -0.648284}]}
