import logging
import sys
logging.basicConfig(level=logging.DEBUG)

from id_auteur import id_Auteur
from id_topics import topic
from analyse_sentiments import sentiment
from extraction_hastags import hashtags
from top_k_hastags import topK_hashtags
from top_K_topics import topK_topics
from top_K_utilisateurs import topK_utilisateurs
from nb_tweets_hastags import tweets_hastags
from nb_tweets_topics import tweets_topics
from nb_tweets_uti import tweets_uti
from traitements_global import service_traitement

from spyne import Application \

from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

from spyne.util.wsgi_wrapper import run_twisted

application1 = Application([hashtags],
    tns='spyne.examples.hello',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

application2 = Application([sentiment],
    tns='spyne.examples.hello',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

application3 = Application([id_Auteur],
    tns='spyne.examples.hello',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

application4 = Application([topic],
    tns='spyne.examples.hello',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

application5 = Application([topK_hashtags],
    tns='spyne.examples.hello',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

application6 = Application([topK_utilisateurs],
    tns='spyne.examples.hello',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

application7 = Application([topK_topics],
    tns='spyne.examples.hello',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

application8 = Application([tweets_uti],
    tns='spyne.examples.hello',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

application9 = Application([tweets_hastags],
    tns='spyne.examples.hello',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

application10 = Application([tweets_topics],
    tns='spyne.examples.hello',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    wsgi_app1 = WsgiApplication(application1)
    wsgi_app2 = WsgiApplication(application2)
    wsgi_app3 = WsgiApplication(application3)
    wsgi_app4 = WsgiApplication(application4)
    wsgi_app5 = WsgiApplication(application5)
    wsgi_app6 = WsgiApplication(application6)
    wsgi_app7 = WsgiApplication(application7)
    wsgi_app8 = WsgiApplication(application8)
    wsgi_app9 = WsgiApplication(application9)
    wsgi_app10 = WsgiApplication(application10)

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8000/%22")
    logging.info("wsdl is at: http://localhost:8000/?wsdl%22")
    
    twisted_apps = [
        (wsgi_app1, b'hashtags'),
        (wsgi_app2, b'sentiment'),
        (wsgi_app3, b'id_Auteur'),
        (wsgi_app4, b'topic'),
        (wsgi_app5, b'topK_hashtags'),
        (wsgi_app6, b'topK_utilisateurs'),
        (wsgi_app7, b'topK_topics'),
        (wsgi_app8, b'tweets_uti'),
        (wsgi_app9, b'tweets_hastags'),
        (wsgi_app10, b'tweets_topics')
        ]

    sys.exit(run_twisted(twisted_apps, 8000))
    