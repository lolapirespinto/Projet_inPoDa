import logging
import sys
logging.basicConfig(level=logging.DEBUG)

from textblob import TextBlob

from spyne import rpc, ServiceBase, \
    Unicode, Float

class sentiment(ServiceBase):
    @rpc(Unicode, _returns=Float)
    def analyse_sentiment(ctx, tweet):
        testimonial = TextBlob(tweet)
        return testimonial.sentiment.polarity



