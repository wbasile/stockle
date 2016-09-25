from stockleapi import finance, reddit, twitter, news
import json
import logging as log

log.basicConfig(level=log.INFO,
                filename='cache/update.log',
                format='%(asctime)s %(message)s')

log.info('reading NASDAQ queries')
company_queries = dict()
with open('nasdaq100.csv') as f:
    for line in f:
        symbol, name, query = line.rstrip().split(',')
        company_queries[symbol] = query

log.info('cache update start')

titles = ["AAPL", "ADBE","EBAY","GOOGL", "MSFT", "YHOO"]
for title in titles:
    log.info('calling finance API for {0}'.format(title))
    dic_finance = finance.get_title(title)
    log.info('writing finance cache for {0}'.format(title))
    with open('cache/finance_{0}.json'.format(title), 'w') as f:
        json.dump(dic_finance, f)
    query = company_queries[title]

    log.info('calling news API for {0}'.format(query))
    news_items = news.get_items(query, cache=False)
    log.info('writing news cache for {0}'.format(title))
    with open('cache/news_{0}.json'.format(title), 'w') as f:
        json.dump(news_items, f)

    log.info('calling reddit API for {0}'.format(query))
    reddit_items = reddit.get_items(query, cache=False)
    log.info('writing reddit cache for {0}'.format(title))
    with open('cache/reddit_{0}.json'.format(title), 'w') as f:
        json.dump(reddit_items, f)

    log.info('calling twitter API for {0}'.format(query))
    twitter_items = twitter.get_items(query, cache=False)
    log.info('writing twitter cache for {0}'.format(title))
    with open('cache/twitter_{0}.json'.format(title), 'w') as f:
        json.dump(twitter_items, f)

log.info('cache update end')
