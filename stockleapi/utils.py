"""
This module contains helper functions binding together different APIs.
"""
from alchemy import AlchemyAPI

# Create the AlchemyAPI Object
alchemy = AlchemyAPI()

def get_sentiment(data, source='text', mode='general', query=None):
    """
    Call the appropriate function from the AlchemyAPI wrapper with the
    right parameters.
    Input:
        data: the text or the URL to analyze.
        source: 'text' or 'url', depending on the input to analyze.
        mode: 'general' performs sentiment analysis on the whole document,
              'targeted' returns the sentiment of the entity specified in the
              query parameter.
        query: entity to target for sentiment analysis (optional).
    Output:
        A real number between -1.0 and 1.0 describing the general or targeted
        sentiment polarity of the document. -1 is negative, 1 is positive.
        Returns None if asking for targeted sentiment the query entity is not
        found in the document.
    """
    if mode == 'general':
        response_sentiment = alchemy.sentiment(source, data)
    elif mode == 'targeted':
        response_sentiment = alchemy.sentiment_targeted(source, data, query)
    else:
        return ValueError('mode cannot be {0}'.format(mode))

    try:
        sentiment = response_sentiment['docSentiment']['type']
    except:
        ''' If the targeted entity is not found in the text the statement above
        will fail.'''
        return None

    if sentiment == 'positive' or sentiment == 'negative':
        sentiment_score = eval(response_sentiment['docSentiment']['score'])
    else:
        # if the sentiment is neutral, the score is zero
        sentiment_score = 0.0

    return sentiment_score
