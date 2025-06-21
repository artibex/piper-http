#/bin/bash

readarray -d '?' -t parts <<< "$MODEL_DOWNLOAD_LINK"
baseurl="${parts[0]%$'\n'}"
params="${parts[-1]%$'\n'}"
readarray -d '/' -t parts <<< "$baseurl"
filename="${parts[-1]%$'\n'}"

# Download onnx file
mkdir -p "$MODEL_TARGET_FOLDER"
wget -c "${MODEL_DOWNLOAD_LINK}" -O "${MODEL_TARGET_FOLDER}/${filename}"

# Download onnx.json file
wget -c "${baseurl}.json?${params}" -O "${MODEL_TARGET_FOLDER}/${filename}.json"

python -m piper.http_server -m "${MODEL_TARGET_FOLDER}/${filename}"
