from flask import Flask, jsonify, send_file
import json
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Path to your JSON file
json_file_path = "dane_telemetryczne_2024-08-20_22-55-18.json"

# Function to read and format JSON data from the file
def read_json_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            return format_data(data)
    else:
        return {"error": "File not found"}

# Function to format the telemetry data
def format_data(data):
    # Format the telemetry data similar to the first code
    formatted_data = {
        "Roll": [round(value, 2) for value in data.get("Roll", [])],
        "Pitch": [round(value, 2) for value in data.get("Pitch", [])],
        "Yaw": [round(value, 2) for value in data.get("Yaw", [])],
        "Latitude": [data.get("Latitude", [])],
        "Longitude": [data.get("Longitude", [])],
        "Altitude": [alt / 1e3 for alt in data.get("Altitude", [])],
        "HDOP": [hdop / 100.0 for hdop in data.get("HDOP", [])],
        "VDOP": [vdop / 100.0 for vdop in data.get("VDOP", [])],
        "Satellites": data.get("Satellites", []),
        "Flight_Mode": data.get("Flight_Mode", []),
        "Voltage": [round(voltage, 2) for voltage in data.get("Voltage", [])],
        "Current": [round(current, 2) for current in data.get("Current", [])],
        "Armed": data.get("Armed", [])
    }
    return formatted_data

@app.route('/api/telemetry', methods=['GET'])
def get_telemetry():
    try:
        data = read_json_file(json_file_path)
        print(data)
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
