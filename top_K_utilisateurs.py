import logging
from collections import Counter
logging.basicConfig(level=logging.DEBUG)

from spyne import rpc, ServiceBase, \
    Integer, Unicode, Array

class topK_utilisateurs(ServiceBase):
    @rpc(Array(Unicode),Integer,_returns=Array(Unicode))
    def top_K_utilisateurs(ctx,k,liste):
        top_k = []
        for i in range(k):
            #récupère l'utilisateur le plus récurrent de la liste 
            max = Counter(liste).most_common(1)[0][0]
            top_k.append(max)
            #ssupprime l'utilisateur pour regarder ensuite les autres
            liste = list(filter(lambda x: x != max, liste))
        return top_k
