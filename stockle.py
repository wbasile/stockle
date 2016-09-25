from stockleapi import finance, reddit, twitter, news
import numpy as np
import random

import json
import plotly

from flask import Flask,render_template
app = Flask(__name__)



def get_graph_data(values):
    
    avg = np.mean(values)
    
    f = float(avg+1) / (2.0)
    # linearly interpolate that value between the colors red and green
    r, g, b = 1-f, f, 0.
    color = '#%02x%02x%02x' % (int(r*255), int(g*255), b)
   
    
    return dict(
            data=[
                {
                    'x': values,
                    #~ 'x': [0.2],
                    'marker': {
                                'color': color,
                                },
                    'boxmean': False,
                    'orientation': 'h',
                    "type": "box",
                
                },
            ],
            
            layout={
                    'autosize': False,
                      'width': 140,
                      'height': 50,
                      'margin': {
                        'l': 0,
                        'r': 0,
                        'b': 0,
                        't': 0,
                        'pad': 1
                      },
                      'paper_bgcolor': '#ffffff',
                      'plot_bgcolor': '#ffffff',
                          
            
                    'xaxis': {
                            'range':[-1,1],
                            'zeroline': True,
                            'showticklabels':False,
                        },
                    'yaxis':{
                        'showticklabels':False,
                    },
                }   

        )
        
    

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
    
    graph_ids = []
    
    graph_data = []

    for t in titles:
        dic_finance = finance.get_title(t)
        #~ dic_finance = {"symbol":t,"name":t, "price":random.random()*100,"change" : random.random()*4 - 2}

        news_items = news.get_items(t)["items"]
        #~ avg_news_sentiment = np.mean([x["sentiment"] for x in news_items])
        #~ dic_finance["sentiment_news"] = avg_news_sentiment

        reddit_items = reddit.get_items(t)["items"]
        #~ avg_reddit_sentiment = np.mean([x["sentiment"] for x in reddit_items])
        #~ dic_finance["sentiment_reddit"] = avg_reddit_sentiment

        twitter_items = twitter.get_items(t)["items"]
        #~ avg_twitter_sentiment = np.mean([x["sentiment"] for x in twitter_items])
        #~ dic_finance["sentiment_twitter"] = avg_twitter_sentiment

        # values for graphs
        graph_ids += [t+"_graph-summary-reddit"]
        graph_data += [get_graph_data([x["sentiment"] for x in reddit_items])]
        
        graph_ids += [t+"_graph-summary-twitter"]
        graph_data += [get_graph_data([x["sentiment"] for x in twitter_items])]
        
        graph_ids += [t+"_graph-summary-news"]
        graph_data += [get_graph_data([x["sentiment"] for x in news_items])]
        
        

        title_list += [dic_finance]


    graph_JSON = json.dumps(graph_data, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template('template_summary.html', title_list=title_list,graph_ids=graph_ids,
                           graph_JSON=graph_JSON)



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
