from flask import Flask, jsonify, send_file
import json
import os

app = Flask(__name__)

# Path to your JSON file
json_file_path = "dane_telemetryczne_2024-08-20_22-55-18.json"

# Function to read JSON data from the file
def read_json_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        return {"error": "File not found"}

# Route to servje the JSON data
@app.route('/api/telemetry', methods=['GET'])
def get_telemetry():
    try:
        data = read_json_file(json_file_path)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Optionally, a route to directly serve the file
@app.route('/api/download-telemetry', methods=['GET'])
def download_telemetry():
    try:
        if os.path.exists(json_file_path):
            return send_file(json_file_path, as_attachment=True)
        else:
            return jsonify({"error": "File not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
