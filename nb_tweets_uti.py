from collections import Counter
import logging
import sys
logging.basicConfig(level=logging.DEBUG)
from spyne import rpc, ServiceBase, \
    Unicode, AnyDict,Array

class tweets_uti(ServiceBase):
    @rpc(Array(Unicode), _returns=AnyDict)
    def nb_tweets_uti(ctx, liste):
        nb_uti = Counter(liste)
        return nb_uti