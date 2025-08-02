from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/api/analyze-utiscan', methods=['POST'])
def analyze_utiscan():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    # Here you would normally process the image.
    # For demo, randomly pick a scenario:

    scenarios = [
        {
            "Leukocytes": "Negative",
            "Nitrites": "Negative",
            "Interpretation": "No signs of UTI detected."
        },
        {
            "Leukocytes": "Positive",
            "Nitrites": "Negative",
            "Interpretation": "Possible UTI detected. Please consult your healthcare provider."
        },
        {
            "Leukocytes": "Negative",
            "Nitrites": "Positive",
            "Interpretation": "Possible UTI detected. Please consult your healthcare provider."
        },
        {
            "Leukocytes": "Positive",
            "Nitrites": "Positive",
            "Interpretation": "Strong evidence of UTI. Please see a doctor immediately."
        }
    ]

    result = random.choice(scenarios)

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
