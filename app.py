from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load the model from the pickle file
with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

# Home route to eliminate 404 error on the root URL
@app.route('/')
def home():
    return "Welcome to the DDoS Model API!"

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the POST request
    data = request.get_json(force=True)
    # Assume the input JSON has a key 'features' with a list of feature values
    features = np.array(data['features']).reshape(1, -1)
    # Make prediction using the loaded model
    prediction = model.predict(features)
    # Return the prediction as JSON
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
