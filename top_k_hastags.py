import logging
logging.basicConfig(level=logging.DEBUG)
from collections import Counter

from spyne import rpc, ServiceBase, \
    Integer, Unicode, Array

class topK_hashtags(ServiceBase):
    @rpc(Array(Unicode), Integer, _returns=Array(Unicode))
    def top_K_hashtags(ctx,liste,k):
        top_k = []
        for i in range(k):
            #récupère le hashtag le plus récurrent de la liste 
            max = Counter(liste).most_common(1)[0][0]
            top_k.append(max)
            #supprime le hastag pour regarder ensuite les autres
            liste = list(filter(lambda x: x != max, liste))
        return top_k
    