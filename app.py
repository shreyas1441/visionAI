from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return "Welcome to the prediction API. Use the /predict endpoint to make predictions."

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from headers
    latitude = request.headers.get('latitude')
    longitude = request.headers.get('longitude')

    # Validate input
    if latitude is None or longitude is None:
        return jsonify({'error': 'Please provide both latitude and longitude in the headers'}), 400

    try:
        latitude = float(latitude)
        longitude = float(longitude)
    except ValueError:
        return jsonify({'error': 'Latitude and longitude must be numbers'}), 400

    # Prepare the input for the model
    input_data = np.array([[latitude, longitude]])

    # Make prediction
    try:
        prediction = model.predict(input_data)
    except Exception as e:
        return jsonify({'error': f'Prediction failed: {str(e)}'}), 500

    # Return prediction as JSON
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
