import os
import sys
import requests
import random
from playsound import playsound

# Take textToSpeak as argument or show usage
if len(sys.argv) < 2:
    print("Use this script to send text to piper, get a response and play it.")
    print()
    print("########## USAGE ##########")
    print("Example: python speak.py \"Hello World!\"")
    print("Example 2: python speak.py \"Hello World!\" \"http://localhost:5000\"")
    sys.exit(1)

# Take texttoSpeak as argument
textToSpeak = sys.argv[1]

urlPiper = "http://localhost:5000"

# create random number for filename
outputFilename = "output" + str(random.randint(1,1000000)) + ".wav"

# Create the payload
payload = {'text': textToSpeak}

# try sending request to piper
try:
    r = requests.get(urlPiper, params=payload)
    r.raise_for_status()
except requests.exceptions.RequestException as e:
    print(e)
    print("Could not send request to piper. Exiting.")
    sys.exit(1)

# Save the response to a file
with open(outputFilename, 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)

# Playsound the file
playsound(outputFilename)

# Remove the file
os.remove(outputFilename)