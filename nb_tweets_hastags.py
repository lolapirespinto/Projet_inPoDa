import logging
from collections import Counter
import sys
logging.basicConfig(level=logging.DEBUG)
from spyne import rpc, ServiceBase, \
    Unicode, AnyDict,Array

class tweets_hastags(ServiceBase):
    @rpc(Array(Unicode), _returns=AnyDict)
    def nb_tweets_hastags(ctx, liste):
        nb_hashtags = Counter(liste)
        return nb_hashtags