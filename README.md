# Assignement_1_Song_Recomendation_API_Vector_Similarity
Assignment 1 : Build a Song Recommendation API Using Vector Similarity

# Assignement_1_Song-Recomendation_API_Vector_Similarity
Assignment 1 : Build a Song Recommendation API Using Vector Similarity 


# Assignment: Build a Song Recommendation API Using Vector Similarity 

## Objective: 
Create an API that takes a feature vector (e.g., danceability, energy, etc.) as input and returns the top 10 most similar songs from a preloaded dataset. 

## Preloaded dataset - 
https://drive.google.com/file/d/1i14pJxmoiERePs46TcXhnJDJQKqxrsh-/view?usp=drive_link 

## Requirements 
### 1. Input:
 A JSON object containing a song's feature vector. 
### 2. Output: 
JSON list of top 10 similar songs with similarity scores and metadata (track 
name, artist, album, etc.). 
### 3. Similarity Metric: 
Cosine similarity (or Euclidean distance if preferred). 
### 4. Framework: 
Flask API (preferred)  
### 5. Data Loading: 
Use the provided CSV to load and cache song features on startup. 

## Tasks 
### 1. Data Preprocessing 
○ Read the CSV  
○ Store both the original song metadata in Elastic Search (preferred) 
### 2. Model Building 
○ Use a NearestNeighbors model (from sklearn.neighbors) with cosine or Euclidean metric. 
### 3. API Development 
○ Create a REST API endpoint /recommend that: 
■ Accepts a POST request with a feature vector. 
■ Finds the top 10 nearest songs using the NearestNeighbors model. 
■ Returns song metadata and similarity scores in the response. 
### 4. Test & Deploy 
○ Test the API with example inputs from the dataset. 
 

## Example Input 
### json 
### POST /recommend 
{ 
  "features": [0.688, 0.481, 6, -8.807, 1, 0.105, 0.289, 0.0, 0.189, 
0.666, 98.017] 
} 
 
## Example Output 
### json 
[ 
  { 
    "track_name": "Days I Will Remember", 
    "artist": "Tyrone Wells", 
    "similarity": 0.98 
  }, 
  { 
    "track_name": "Hold On", 
    "artist": "Chord Overstreet", 
    "similarity": 0.91 
  }, 
  ... 
] 
 
## Feature Columns to Use 
● danceability, energy, key, loudness,mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo 

## Tools and Libraries 
● Python 
● Pandas 
● Scikit-learn 
● Flask 

## Terminal Comands for the python virtual environment
### setup initialization :-
python -m venv venv
### install dependencies :-
python install -r requirements.txt
### activate :- 
.\tf-env\Scripts\Activate.ps1
### deactivate :- 
deactivate

## Terminal Comands for the ElastiSearch - Docker environment
### docker run :-
docker run -d --name elasticsearch -p 9200:9200 -e "discovery.type=single-node" -e "xpack.security.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:8.13.4
