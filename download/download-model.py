# Use this script to download a .onnx model and a .json via wget
# Provide a direct download link to the .onnx file and the .json file as arguments

# Using the wget library

import subprocess
import wget
import sys
import os


# If no args are provided, exit
if len(sys.argv) < 3:
    print("No link provided, please proved a .onnx download link and a .json download link and a target folder.")
    exit()

# Get model link as argument
link_model = sys.argv[1]

# Get json link as argument
link_json = sys.argv[2]

# Get folder where the script is running
folder = os.path.dirname(os.path.abspath(__file__))

# If sys.argv[3] is provided, use it as target folder
if len(sys.argv) > 3:
    target_folder = sys.argv[3]
else:
    # If target folder is not provided, use the current folder
    target_folder = folder

# Build filename with current folder
filename_model = os.path.join(target_folder, "model.onnx")

# Get the .json filename by adding .json to the .onnx filename
filename_json = filename_model + ".json"

# Use subprocess and getfile.py to download the .onnx and .json file
subprocess.run(['python', f"{folder}/getfile.py", link_model, filename_model])
subprocess.run(['python', f"{folder}/getfile.py", link_json, filename_json])