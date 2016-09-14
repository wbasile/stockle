import yaml
import requests
from requests_oauthlib import OAuth1
import json
import logging as log
from os.path import join, dirname

# read the configuration file
with open(join(dirname(__file__),'config/config.yaml')) as fd_conf:
    config = yaml.load(fd_conf)

# OAuth 1 authentication
auth = OAuth1(config['consumer_key'],
              config['consumer_secret'],
              config['oauth_token'],
              config['oauth_secret'])

def get_keywords_stream(keyword):
    # POST data: list of keywords to search
    data = {'track':keyword}
    response = requests.post(config['url_filter'], data=data, auth=auth, stream=True)

    tweets = []
    for line in response.iter_lines():
        if line:
            try:
                tweet = json.loads(line)
                tweets.append(json.dumps(tweet))
            except:
                log.error('error parsing tweet')
        if len(tweets) >= config['response_size']:
            break
    return tweets
