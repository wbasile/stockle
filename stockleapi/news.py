import random

def get_items(query,n=10):
    items = {'items':[]}

    for i in range(n):
        item = {}
        item["title"] = "news article about " + query + " " + str(i)
        item["url"] = "http://www.blahblah.com/news_article_" + query + "_" + str(i)
        item["sentiment"] = random.random() * 2 - 1

        items['items'].append(item)

    return items
