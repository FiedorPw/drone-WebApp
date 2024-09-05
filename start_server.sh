#!/bin/bash

# -m dla mock

# Get the IP address of wlan0
WLAN0_IP=$(ip -4 addr show wlan0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}')

# ustaiwanie ip z palca
# WLAN0_IP="192.168.77.183"

# Export ip jako zmienna globalna
export WLAN0_IP

# Print ip
echo -e "\033[0;35mWLAN0 IP Address: $WLAN0_IP"

# odpalanie frontu port 80
nohup npm --prefix ./FrontEnd/ run dev &

# odpalanie backu port 5000
if [[ "$1" == "-m" ]]; then
    # If -m flag is present, run the mock backend
    echo -e "\033[1;36mRunning mock backend..."
    nohup python ./Mock_BackEnd/Backend.py &
else
    # Otherwise, run the regular backend
    echo -e "\033[1;36mRunning regular backend..."
    nohup python ./BackEnd/Backend.py &
fi
sleep 0.2
# odpalanie cockpit port 9090
sudo systemctl start cockpit

firefox-esr $WLAN0_IP &

# mjpg streamer kamerki port 8080

# na dronie
sudo systemctl start mjpg-streamer.service
# albo
# /snap/bin/mjpg-streamer -i "input_uvc.so -d /dev/video0" -o "output_http.so -w /usr/share/mjpg-streamer/www -p 8080"
# lokalnie
mjpg_streamer -i "input_uvc.so -d /dev/video0 -r 640x480 -f 30" -o "output_http.so -w ./www"
