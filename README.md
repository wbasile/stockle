# stockle
A dashboard of news and sentiment for your financial trade

Stockle is a Web app and an API that provides sentiment analysis of
the stock trade market. The user follows a set of companies, and the 
API retrieves news, reddit comment threads and tweets from
Twitter. Each item is associated with an indicator of the sentiment
towards the company, shown as a box plot of its distribution. The
aggregated sentiment is also shown per each source of information.

Stockle API is a wrapper around the APIs of Yahoo Finance, reddit,
Twitter, and AlchemyData News. It uses Alchemy Sentiment API to
extract the sentiment information from texts and URLs.  The app
searches for company names in the news and on social media, then 
calls Alchemy API to get the targeted sentiment towards the company in the
retrieved texts.

Live demo:           http://gingerbeard.alwaysdata.net/stockle/
Presentation slides: https://www.slideshare.net/secret/gsHP02vLAigG5y

