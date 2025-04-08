import pandas as pd
from sklearn.preprocessing import StandardScaler

FEATURE_COLUMNS=['danceability', 'energy', 'key', 'loudness', 'mode','speechiness', 'acousticness', 'instrumentalness','liveness', 'valence', 'tempo']

def load_data(filepath):
    df = pd.read_csv(filepath)
    features = df[FEATURE_COLUMNS]
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    return df, scaled_features, scaler