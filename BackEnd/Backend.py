from pymavlink import mavutil
import os
import json
import time
import math
from datetime import datetime
import shutil
from threading import Thread, Lock
from flask import Flask, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Directory to read logs
log_dir = "/home/KNR/KNR-dron/LOGS/"


# Initialize telemetry data and log rotation settings
telemetry_data = {
    "Roll": [],
    "Pitch": [],
    "Yaw": [],
    "Latitude": [],
    "Longitude": [],
    "Altitude": [],
    "HDOP": [],
    "VDOP": [],
    "Satellites": [],
    "Flight_Mode": [],
    "Voltage": [],
    "Current": [],
    "Armed": []
}

# Lock for thread-safe file operations
file_lock = Lock()

# Track number of saves and the current log filename
save_count = 0

# Function to return the path of the lastly modified file in the directory
def get_last_modified_file(dir_path):
    files = [os.path.join(dir_path, f) for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    if not files:
        return None
    return max(files, key=os.path.getmtime)

# Function to read telemetry data from JSON file
def read_from_json():
    log_path = get_last_modified_file(log_dir)
    if log_path is None:
        raise FileNotFoundError("No log files found.")
    with open(log_path, 'r') as json_file:
        return json.load(json_file)

# Flask route to serve telemetry data
@app.route('/api', methods=['GET'])
def get_telemetry():
    try:
        data = read_from_json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
