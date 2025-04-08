from flask import Flask, request, jsonify
from flask_cors import CORS
from threading import Thread
import traceback

from utils import load_data, FEATURE_COLUMNS
from recomender import create_model, recommend
from es_helper import get_es_client, create_index, index_song_metadata

app = Flask(__name__)
CORS(app)  

filepath = 'cleaned_dataset.csv'
df, scaled_features, scaler = load_data(filepath)
recommender = create_model(scaled_features)

es_client = get_es_client()
create_index(es_client)

def index_data():
    try:
        print("Indexing data in background")
        index_song_metadata(es_client, df)
        print("Finished indexing dataset into Elasticsearch")
    except Exception as e:
        print("Error during background indexing:")
        traceback.print_exc()

Thread(target=index_data, daemon=True).start()

@app.route("/")
def hello_world():
    return "<p>Song Recommendation API Running</p>"

@app.route("/health")
def health_check():
    return jsonify({"status": "ok"})

@app.route('/recommend', methods=['POST'])
def recommendation():
    try:
        data = request.get_json(force=True)
        input_vector = data.get("features")

        if not input_vector or len(input_vector) != len(FEATURE_COLUMNS):
            return jsonify({"error": f"Input vector must have {len(FEATURE_COLUMNS)} features."}), 400

        try:
            input_vector_scaled = scaler.transform([input_vector])[0]
        except Exception as e:
            return jsonify({"error": "Scaler transformation failed.", "details": str(e)}), 500

        distances, indices = recommend(recommender, input_vector_scaled)

        recommendations = []
        for dist, idx in zip(distances, indices):
            track_name = df.iloc[idx]['track_name']

            try:
                resp = es_client.search(index="songs", query={
                    "match": {"track_name": track_name}
                })

                if resp['hits']['hits']:
                    song = resp['hits']['hits'][0]['_source']
                else:
                    song = {
                        "track_name": track_name,
                        "artists": df.iloc[idx].get('artists', 'Unknown')
                    }

            except Exception:
                song = {
                    "track_name": track_name,
                    "artists": df.iloc[idx].get('artists', 'Unknown')
                }

            similarity = max(0.0, min(1.0, round(1 - dist, 3)))
            recommendations.append({
                "track_name": song['track_name'],
                "artists": song['artists'],
                "similarity": similarity
            })


        return jsonify(recommendations)

    except Exception as e:
        print("Exception in /recommend:")
        traceback.print_exc()
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

if __name__ == '__main__':
    port = 8080
    print(f"Starting Flask server on http://127.0.0.1:{port}")
    app.run(debug=True, port=port, use_reloader=False)
