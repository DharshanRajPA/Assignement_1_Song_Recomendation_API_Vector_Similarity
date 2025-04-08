import numpy as np
from sklearn.neighbors import NearestNeighbors

def create_model(features,metric='cosine'):
    model=NearestNeighbors(n_neighbors=10, metric=metric)
    model.fit(features)
    return model

def recommend(model,input_vector):
    distances, indices = model.kneighbors([input_vector])
    return distances[0], indices[0]