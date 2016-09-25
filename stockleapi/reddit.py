"""
Wrapper around the reddit API using the PRAW library.
"""

import random
import config
import praw
import utils
import json

def get_items(query, cache=True, mock=False):
    """
    Access the reddit API, search for the input keyword. For each post take
    the concatenation of all the comments and pass it to the sentimentanalysis
    API (AlchemyAPI). Returns a list of reddit threads with a sentiment score.

    Input: a string containing the name of a company.
    Output: JSON containing a list of items (title, URL, sentiment)
    """

    if cache:
        with open('cache/reddit_{0}.json'.format(query)) as f:
            items = json.loads(f.read())
        return items
    elif mock:
        return {'items': [
                 {'url': u'https://www.reddit.com/r/iiiiiiitttttttttttt/comments/536twc/someone_i_know_said_that_their_ancient_win_xp/?ref=search_posts',
                  'sentiment': -0.163568,
                  'title': u'Someone I know said that their ancient, Win XP IBM-era Thinkpad is getting slow and asked if I could do a clean windows install to make it faster. Boot to login: 40 seconds. Boot to usable desktop: sub 2 minutes.'},
                 {'url': u'https://www.reddit.com/r/retrobattlestations/comments/536p70/ibm_5100_from_1975/?ref=search_posts',
                  'sentiment': 0.615872,
                  'title': u'IBM 5100 from 1975'},
                 {'url': u'https://www.reddit.com/r/techsupportanimals/comments/536j5x/someone_said_their_ibm_thinkpad_win_xp_runs_slow/?ref=search_posts',
                  'sentiment': -0.0924824,
                  'title': u'Someone said their IBM(!!!) Thinkpad (Win XP) runs slow and asked if I can do a clean Windows install to make it less slow. Thing needs 40 seconds to login and sub-2min to usable desktop. mfw'},
                 {'url': u'https://www.reddit.com/r/melbourne/comments/536fty/i_thought_this_was_a_massive_disappointment_did/?ref=search_posts',
                  'sentiment': 0.0563994,
                  'title': u'I thought this was a massive disappointment. Did it get better later on or was it just a few beams from the IBM building and a green beam from fed square?'},
                 {'url': u'https://www.reddit.com/r/trailers/comments/535z1d/silicon_cowboys_documentary_of_compaq_computer/?ref=search_posts',
                  'sentiment': 0.271896,
                  'title': u"Silicon Cowboys - Documentary of Compaq Computer and it's battle with IBM"}]}
    else:
        items = {'items':[]}

        # use PRAW to search reddit_agent
        r = praw.Reddit(config.reddit_agent)
        posts = r.search(query,sort='new',limit=None,syntax='cloudsearch')

        for post in posts:
            # get a list of the texts of the comments
            comments = praw.helpers.flatten_tree(post.comments)
            try:
                comments_text = reduce(lambda x, y: x+'\n'+y, [comment.body for comment in comments])
            except:
                continue

            # targeted sentiment analysis is too slow, so we just analyze the
            # sentiment of the whole text.

            sentiment_score = utils.get_sentiment(comments_text, 'text', 'general')
            items['items'].append({'title' : post.title,
                                   'url' : post.permalink,
                                   'sentiment' : sentiment_score})

            # stop cycling when reaching the desired item list size
            if len(items['items']) >= config.reddit_list_size:
                break
        return items
