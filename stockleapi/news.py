import random

def get_items(query,n=10):
    item_list = []
    
    for i in range(n):
        item = {}
        item["title"] = "news article about " + query + " " + str(i)
        item["link"] = "http://www.blahblah.com/news_article_" + query + "_" + str(i)
        item["sentiment"] = random.random() * 2 - 1
        
        item_list += [item]
        
    return item_list
    
