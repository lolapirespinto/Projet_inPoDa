import logging
import sys
logging.basicConfig(level=logging.DEBUG)

from spyne import rpc, ServiceBase, \
    Unicode, AnyDict

class id_Auteur(ServiceBase):
    @rpc(AnyDict, _returns=Unicode)
    def identification_auteur(ctx, tweet):
        return tweet["author_id"]



