from stockleapi import finance, reddit, twitter, news
import numpy as np
import random

from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'



@app.route('/summary')
def view_summary():

    titles = ["AAPL","IBM","FB","GOOG"]

    title_list = []

    for t in titles:
        dic_finance = finance.get_title(t)
        #~ dic_finance = {"symbol":t,"name":t, "price":random.random()*100,"change" : random.random()*4 - 2}

        news_items = news.get_items(t)["items"]
        avg_news_sentiment = np.mean([x["sentiment"] for x in news_items])
        dic_finance["sentiment_news"] = avg_news_sentiment

        reddit_items = reddit.get_items(t)["items"]
        avg_reddit_sentiment = np.mean([x["sentiment"] for x in reddit_items])
        dic_finance["sentiment_reddit"] = avg_reddit_sentiment

        twitter_items = twitter.get_items(t)["items"]
        avg_twitter_sentiment = np.mean([x["sentiment"] for x in twitter_items])
        dic_finance["sentiment_twitter"] = avg_twitter_sentiment


        # values for reddit graph
        reddit_graph_start = min([(avg_reddit_sentiment + 1) *  50 ,50])
        if avg_reddit_sentiment < 0:
            reddit_graph_color = "#ff4136"
        else:
            reddit_graph_color = "#36ee41"
        reddit_graph_width = abs(50 - ((avg_reddit_sentiment + 1) *  50))

        dic_finance["sentiment_reddit_graph_start"] = reddit_graph_start
        dic_finance["sentiment_reddit_graph_width"] = reddit_graph_width
        dic_finance["sentiment_reddit_graph_color"] = reddit_graph_color


        # values for twitter graph
        twitter_graph_start = min([(avg_twitter_sentiment + 1) *  50 ,50])
        if avg_twitter_sentiment < 0:
            twitter_graph_color = "#ff4136"
        else:
            twitter_graph_color = "#36ee41"
        twitter_graph_width = abs(50 - ((avg_twitter_sentiment + 1) *  50))

        dic_finance["sentiment_twitter_graph_start"] = twitter_graph_start
        dic_finance["sentiment_twitter_graph_width"] = twitter_graph_width
        dic_finance["sentiment_twitter_graph_color"] = twitter_graph_color


        # values for news graph
        news_graph_start = min([(avg_news_sentiment + 1) *  50 ,50])
        if avg_news_sentiment < 0:
            news_graph_color = "#ff4136"
        else:
            news_graph_color = "#36ee41"
        news_graph_width = abs(50 - ((avg_news_sentiment + 1) *  50))

        dic_finance["sentiment_news_graph_start"] = news_graph_start
        dic_finance["sentiment_news_graph_width"] = news_graph_width
        dic_finance["sentiment_news_graph_color"] = news_graph_color

        title_list += [dic_finance]


    return render_template('template_summary.html', title_list=title_list)



@app.route('/detail/<t>')
def show_title_detail(t):
    # deatails for a given title
    dic_finance = finance.get_title(t)
    #dic_finance = {"name":t, "price":random.random()*100,"change" : random.random()*4 - 2}
    news_items = news.get_items(dic_finance['name'])["items"]
    #avg_news_sentiment = np.mean([x["sentiment"] for x in news_items])
    dic_finance["news"] = news_items

    reddit_items = reddit.get_items(dic_finance['name'])["items"]
    #~ avg_reddit_sentiment = np.mean([x["sentiment"] for x in reddit_items])
    dic_finance["reddit"] = reddit_items

    twitter_items = twitter.get_items(dic_finance['name'])["items"]
    #~ avg_twitter_sentiment = np.mean([x["sentiment"] for x in twitter_items])
    dic_finance["twitter"] = twitter_items


    return render_template('template_detail.html', title = dic_finance)



#~ @app.route('/post/<int:post_id>')
#~ def show_post(post_id):
    #~ # show the post with the given id, the id is an integer
    #~ return 'Post %d' % post_id


if __name__ == "__main__":
    app.run()
