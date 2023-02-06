import logging
import sys
logging.basicConfig(level=logging.DEBUG)
from random import *

from spyne import rpc, ServiceBase, \
    Unicode

class topic(ServiceBase):
    @rpc(_returns=Unicode)
    def identification_topic(ctx):
        topics = ['politique', 'sport' , 'cinema' , 'scientifique']
        topic = choice(topics)
        return topic

