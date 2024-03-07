# Entrypoint script for docker container
# This script will be locatet /app/run.py

import subprocess
import os
import sys

# If no args are provided, explain
if len(sys.argv) < 3:
    print("Usage: python run.py <link> <target_folder>")
    sys.exit(1)

# Get link as sys.argv[1]
link = sys.argv[1]

# Get target folder as sys.argv[2]
target_folder = sys.argv[2]

# Get folder of this script
script_folder = os.path.dirname(os.path.realpath(__file__))

# Join script folder with download-piper-voices.py
download_script = os.path.join(script_folder, "download/download-piper-voices.py")

# Download the model
subprocess.run(['python', download_script, link, target_folder])

# Join target_folder with the model name
model_path = os.path.join(target_folder, "model.onnx")

# If the --speaker arg is provided, run the http server with the model and the speaker
if len(sys.argv) > 3:
    speaker = sys.argv[3]
    subprocess.run(['python', '-m', 'piper.http_server', '-m', model_path, '-s', speaker])
    # sys.exit(0)
else:
    subprocess.run(['python', '-m', 'piper.http_server', '-m', model_path])
    # sys.exit(0)