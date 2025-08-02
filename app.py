from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/analyze-utiscan', methods=['POST'])
def analyze_utiscan():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    
    return jsonify({
        "Leukocytes": "Positive",
        "Nitrites": "Negative",
        "Interpretation": "Possible UTI detected. Please see doctor."
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
