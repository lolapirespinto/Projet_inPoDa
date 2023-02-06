
from suds.client import Client
import logging
logging.basicConfig(level=logging.DEBUG)

def service_global():
    service_traitement = Client('http://127.0.0.1:8000/service_traitement?wsdl')
    service_traitement.service.traitement()

if __name__ == '__main__':
    service_global()