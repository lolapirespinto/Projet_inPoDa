import logging
import sys
logging.basicConfig(level=logging.DEBUG)
from collections import Counter

from spyne import rpc, ServiceBase, \
    Unicode, Array, Integer

class topK_topics(ServiceBase):
    @rpc(Array(Unicode),Integer,_returns=Array(Unicode))
    def top_K_topics(ctx,k,liste):
        top_k = []
        for i in range(k):
            #récupère le topic le plus récurrent de la liste 
            max = Counter(liste).most_common(1)[0][0]
            top_k.append(max)
            #supprime le topic pour regarder ensuite les autres
            liste = list(filter(lambda x: x != max, liste))
        return top_k