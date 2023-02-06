import re
import logging
import sys
logging.basicConfig(level=logging.DEBUG)

from spyne import rpc, ServiceBase, \
    Unicode, Array

class hashtags(ServiceBase):
    @rpc(Unicode, _returns=Array(Unicode))
    def extraction_hashtags(ctx, tweet):
        return re.findall(r"#(\w+)", tweet) if "#" in tweet else [""]
        


