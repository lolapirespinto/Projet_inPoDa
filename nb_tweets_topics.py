import logging
from collections import Counter
import sys
logging.basicConfig(level=logging.DEBUG)
from spyne import rpc, ServiceBase, \
    Unicode, AnyDict,Array

class tweets_topics(ServiceBase):
    @rpc(Array(Unicode), _returns=AnyDict)
    def nb_tweets_topics(ctx, liste):
        nb_topics = Counter(liste)
        return nb_topics