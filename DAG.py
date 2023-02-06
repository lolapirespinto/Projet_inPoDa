from datetime import datetime
from pymongo import MongoClient
from suds.client import Client
from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

#Tasks are represented as operators
client = MongoClient('mongodb://localhost:27017');

#La base de données
db_name = 'Projet_SOA'
db = client[db_name]
        
#Collection de tweets 
coll_name = "traitement_tweets"
coll = db[coll_name]


with DAG(dag_id="demo", start_date=datetime(2022, 1, 1), schedule="0 0 * * *") as dag:

    tweets = [t for t in coll.find()]
    results = {}

    @task()
    def get_autheur(**kwargs):
        for t in tweets: 
            if not t["id"] in results:
                results[t["id"]] = {} 
            results[t["id"]]["auteur"] = t["author_id"]
        kwargs['ti'].xcom_push(key='results', value=results)
        return results
        
    @task()
    def get_topic(**kwargs): 
        results = kwargs['ti'].xcom_pull(key='results', task_ids='get_autheur')
        topic = Client('http://127.0.0.1:8000/topic?wsdl')
        print(results) # Devrait maintenant afficher les résultats de get_autheur
        for t in tweets: 
            if not t["id"] in results:
                results[t["id"]] = {} 
            results[t["id"]]["topic"] = topic.service.identification_topic()
        kwargs['ti'].xcom_push(key='results', value=results)
        return results

    @task()
    def get_sentiment(**kwargs):
        results = kwargs['ti'].xcom_pull(key='results', task_ids='get_topic')
        sentiment = Client('http://127.0.0.1:8000/sentiment?wsdl')
        for t in tweets: 
            if not t["id"] in results:
                results[t["id"]] = {} 
            results[t["id"]]["sentiment"] = sentiment.service.analyse_sentiment(t["text"])
        kwargs['ti'].xcom_push(key='results', value=results)
        return results
        
    @task()
    def get_hashtags(**kwargs):
        results = kwargs['ti'].xcom_pull(key='results', task_ids='get_sentiment')
        liste_hashtags = []
        hashtags = Client('http://127.0.0.1:8000/hashtags?wsdl')
        for t in tweets: 
            if not t["id"] in results:
                results[t["id"]] = {} 
            liste_hashtags += [i[1] for i in hashtags.service.extraction_hashtags(t["text"])]
            results[t["id"]]["hashtags"] = liste_hashtags
            liste_hashtags = []
        kwargs['ti'].xcom_push(key='results', value=results)
        client.close();
        return results

    @task()
    def show_results(**kwargs):
        results = kwargs['ti'].xcom_pull(key='results', task_ids='get_hashtags')
        print(results)

    #Set dependencies between tasks
    get_autheur() >> get_topic() >> get_sentiment() >> get_hashtags() >> show_results()