import os
import sys
import subprocess
import tempfile
import requests

# Take textToSpeak as argument or show usage
if len(sys.argv) < 2:
    print("Use this script to send text to piper, get a response and play it.")
    print()
    print("########## USAGE ##########")
    print("Example: python piper-tts.py \"Hello World!\"")
    print("Example 2: python piper-tts.py \"Hello World!\" \"http://localhost:5000\"")
    sys.exit(1)

# Take textToSpeak as argument
textToSpeak = sys.argv[1]

# Optional: custom piper URL as second argument
urlPiper = sys.argv[2] if len(sys.argv) > 2 else "http://localhost:5000"

# Create the payload
payload = {'text': textToSpeak}

# Try sending request to piper
try:
    r = requests.get(urlPiper, params=payload)
    r.raise_for_status()
except requests.exceptions.RequestException as e:
    print(e)
    print("Could not send request to piper. Exiting.")
    sys.exit(1)

# Save response to a temporary WAV file and play it
with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
    tmp.write(r.content)
    tmpfile = tmp.name

try:
    # Try players in order of preference: pw-play (PipeWire), paplay (PulseAudio),
    # mpv, ffplay – use whichever is installed
    players = ["pw-play", "paplay", "mpv", "ffplay"]
    played = False
    for player in players:
        result = subprocess.run(["which", player], capture_output=True)
        if result.returncode == 0:
            subprocess.run([player, tmpfile], check=True)
            played = True
            break
    if not played:
        print("No audio player found. Install one of: pw-play, paplay, mpv, ffplay")
        print(f"WAV file saved at: {tmpfile}")
        sys.exit(1)
finally:
    os.remove(tmpfile)