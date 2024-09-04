#!/bin/bash

# Get the IP address of wlan0
WLAN0_IP=$(ip -4 addr show wlan0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}')

# ustaiwanie ip z palca
# WLAN0_IP="192.168.77.183"

# Export ip jako zmienna globalna
export WLAN0_IP

#print ip
echo "WLAN0 IP Address: $WLAN0_IP"

# odpalanie frontu port 3000
nohup npm --prefix ./FrontEnd/ run dev &
# odpalanie backu port 5000
nohup python ./BackEnd/Backend.py &
# kamerki port 8080
sudo systemctl start mjpg-streamer.service
# odpalanie cockpit port 9090
sudo systemctl start cockpit