#!/bin/bash

# Check if python3-venv is installed
if ! dpkg -l | grep -q python3-venv; then
    echo "python3-venv is not installed. Installing..."
    sudo apt-get update
    sudo apt-get install -y python3-venv
else
    echo "python3-venv is already installed."
fi

# Create a virtual environment in the current directory
python3 -m venv ./venv

echo "Virtual environment created at ./venv"

# Activate the virtual environment
source ./venv/bin/activate

# Install the requirements
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
    echo "Requirements installed."
else
    echo "requirements.txt not found."
fi

python person_recognition.py
