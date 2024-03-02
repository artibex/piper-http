# Get a link to a model from huggingface and download it into the current folder.
# The link should be the DIRECT  link to the .onnx file. 
# # The script will also download the .json in the same folder.


# Using the wget library
import subprocess
import wget
import sys
import os


# Get the model from huggigface repo from piper-voices
# Example link for .onnx: https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/de/de_DE/mls/medium/de_DE-mls-medium.onnx?download=true
# Example link for .json: https://huggingface.co/rhasspy/piper-voices/raw/v1.0.0/de/de_DE/mls/medium/de_DE-mls-medium.onnx.json


# If no argument is given, print usage
if len(sys.argv) < 3:
    print("Usage: python download-piper-voice.py <link> <target_folder>")
    sys.exit(1)

link_model = sys.argv[1]
target_folder = sys.argv[2]

# Get folder where the script is running
folder = os.path.dirname(os.path.abspath(__file__))

# Remove the ?download=true from the link
link_json = link_model.split('?')[0]

# Add .json to the link
link_json = link_json + ".json"

# Use download.py to download the .onnx file and the .json file which is in this folder
subprocess.run(['python', f"{folder}/download-model.py", link_model, link_json, target_folder])
