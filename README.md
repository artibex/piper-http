# piper-http
Creates a docker image that runs the piper http service found in this repo:
https://github.com/rhasspy/piper

Docker Hub image: https://hub.docker.com/r/artibex/piper-http

---

## Quickstart

The fastest way to get started is with Docker Compose using the pre-built image from Docker Hub.

**1. Clone the repository**
```bash
git clone https://github.com/artibex/piper-http.git
cd piper-http
```

**2. Start the service**
```bash
docker compose up -d
```

That's it. The container pulls `artibex/piper-http:latest` from Docker Hub, downloads the default German voice on first start, and serves the HTTP API on port **5000**.  
The downloaded model is stored in a named Docker volume (`piper-models`) so it is only downloaded once.

**3. Test it**
```bash
curl "http://localhost:5000/?text=Hello+World" -o hello.wav
```

**Change the voice** by editing `MODEL_DOWNLOAD_LINK` in `docker-compose.yml` and restarting:
```bash
docker compose up -d
```
Browse available voices: https://huggingface.co/rhasspy/piper-voices

---

## Python client

Send text and play the audio directly:

```bash
pip install requests
python client/piper-tts.py "Hello World!"
# Optional: custom server URL
python client/piper-tts.py "Hello World!" "http://localhost:5000"
```

> Requires one of these audio players (used in order): `pw-play`, `paplay`, `mpv`, `ffplay`

---

## Manual setup (build your own image)

1. Clone the repository and navigate into it
2. `docker build -t piper .`
3. `docker run --name piper -p 5000:5000 piper`

Or run the pre-built Docker Hub image directly without cloning:
```bash
docker run -d --name piper -p 5000:5000 \
  -e MODEL_DOWNLOAD_LINK="https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/kusal/medium/en_US-kusal-medium.onnx?download=true" \
  artibex/piper-http
```

---

### Support the Developer:
- [Buy Me a Coffee](https://buymeacoffee.com/artibex)
- [My Music / Socials](https://hyperfollow.com/Artibex)
