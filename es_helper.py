from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

def get_es_client():
    return Elasticsearch("http://localhost:9200")

def create_index(es_client):
    if not es_client.indices.exists(index="songs"):
        es_client.indices.create(index="songs")

def index_song_metadata(es_client, df):
    actions = []
    for _, row in df.iterrows():
        action = {
            "_index": "songs",
            "_source": {
                "track_name": row['track_name'],
                "artists": row['artists'],
                "popularity": row['popularity'],
                "danceability": row['danceability'],
                "energy": row['energy'],
                "valence": row.get('valence', 0),
                "tempo": row.get('tempo', 0),
            }
        }
        actions.append(action)

    bulk(es_client, actions)
