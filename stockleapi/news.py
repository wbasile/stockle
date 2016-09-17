import random
import requests
import config
import utils

'''
def get_items(query):
    data = {'apikey':config.alchemyapi_key ,
            'outputMode':'json',
            'start':'now-1d',
            'end':'now',
            #'count':config.news_list_size,
            'q.enriched.url.title':query,
            'return':'original.url,enriched.url.title'}
    response = requests.get(config.url_news, params=data)
    results = response.json()
    items = {'items':[]}
    for item in results['result']['docs']:
        sentiment_score = utils.get_sentiment(item['source']['original']['url'], 'url', 'targeted', query)
        if sentiment_score:
            items['items'].append({'title' : item['source']['enriched']['url']['title'],
                                   'url' : item['source']['original']['url'],
                                   'sentiment' : sentiment_score})
        # stop cycling when reaching the desired item list size
        if len(items['items']) >= config.tweet_list_size:
            break
    return items
'''

def get_items(query):
    return {'items': [
             {'url': u'http://finance.yahoo.com/m/274e68d5-b53b-3a13-b5fe-0686b4f501f4/apple-end-four-day-winning.html?guid=096BAA7E-7C17-11E6-AA97-CF05589A95D8&siteid=yhoof2&yptr=yahoo',
             'sentiment': -0.412696,
             'title': u'Apple end four-day winning streak'},
            {'url': u'https://itunes.apple.com/us/post/idsa.09ce2c03-a1b4-11e5-8838-cb4822dc8c3d',
             'sentiment': 0.299896,
             'title': u'Watch \u201cThe 1989 World Tour \u2014 Live (Preview)\u201d posted by Taylor Swift on Apple Music.'},
            {'url': u'http://uk.reuters.com/article/uk-apple-japan-tax-idUKKCN11M09M?il=0',
             'sentiment': -0.571383,
             'title': u'Apple Japan unit ordered to pay $118 million tax for underreporting income - media'},
            {'url': u'http://finance.yahoo.com/news/apple-lifts-tech-etfs-during-140000778.html',
             'sentiment': -0.168371,
             'title': u'Apple Lifts Tech ETFs During Market Slump'},
            {'url': u'https://ca.news.yahoo.com/apple-stock-heads-best-four-days-since-2014-170818906--finance.html',
             'sentiment': -0.446473,
             'title': u'Apple stock heads for best four days since 2014; short sellers flee'}]}
