# OAuth credential for the Twitter API
consumer_key = ""
consumer_secret = ""
oauth_token = ""
oauth_secret = ""

# URL of the Twitter API for the keyword search stream
url_twitter = 'https://api.twitter.com/1.1/search/tweets.json'

# base URL of the AlchemyData News API
url_news = 'http://gateway-a.watsonplatform.net/calls/data/GetNews'

# how may tweets are returned
tweet_list_size = 50

# how may news items are returned
news_list_size = 50

# key for Alchemy API
alchemyapi_key = ""

try:
    from .config_local import *
except ImportError:
    pass
