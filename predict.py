from flask import request, jsonify
import joblib
import os

# Load model once
model_path = os.path.join(os.path.dirname(__file__), "../model/model.pkl")
model = joblib.load(model_path)

def predict_price():
    data = request.get_json()

    # Example input keys: ['Latitude', 'Longitude', 'Beds', 'Baths', 'Postcode_score']
    features = ['Latitude', 'Longitude', 'Beds', 'Baths', 'Postcode_score']
    input_data = [data.get(key, 0) for key in features]

    prediction = model.predict([input_data])[0]
    return jsonify({"predicted_price": round(prediction, 2)})
