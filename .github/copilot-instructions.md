# piper-http – Copilot Instructions

## Project Overview
`piper-http` wraps the [Piper TTS engine](https://github.com/rhasspy/piper) in a lightweight HTTP server and packages it as a Docker image.  
Clients send plain-text GET requests to port **5000** and receive a WAV audio stream in return.

## Repository Layout
```
piper-http/
├── Dockerfile                  # Multi-stage build – clones piper, installs deps, copies run.py
├── run.py                      # Container entrypoint: downloads model (if missing), starts HTTP server
├── README.md
├── client/
│   └── piper-tts.py            # Example client: sends text → receives WAV → plays audio
└── download/
    ├── download-piper-voices.py  # High-level helper: derives .json URL from .onnx URL, calls download-model.py
    ├── download-model.py         # Downloads model.onnx + model.onnx.json into the target folder
    └── getfile.py                # Low-level wget wrapper
```

## How It Works
1. **Build** – `docker build -t piper .`  
   Clones [rhasspy/piper](https://github.com/rhasspy/piper) and installs `piper[http_server]` from source.
2. **Run** – `docker run -p 5000:5000 piper`  
   `run.py` is the CMD entrypoint. It:
   - Reads `MODEL_DOWNLOAD_LINK`, `MODEL_TARGET_FOLDER`, and `SPEAKER` from environment / CLI args.
   - Checks whether `<MODEL_TARGET_FOLDER>/model.onnx` **already exists** before downloading.
   - Starts `python -m piper.http_server -m <model_path> [-s <speaker>]`.
3. **Request** – `GET http://localhost:5000/?text=Hello+World` → returns `audio/wav`.

## Key Environment Variables (Dockerfile defaults)
| Variable | Default | Description |
|---|---|---|
| `MODEL_DOWNLOAD_LINK` | German pavoque-low .onnx on HuggingFace | Direct download URL for the `.onnx` model file |
| `MODEL_TARGET_FOLDER` | `/app/models` | Directory where model files are stored inside the container |
| `SPEAKER` | `0` | Piper speaker index (for multi-speaker models) |

## Changing the Voice
Pass a different `MODEL_DOWNLOAD_LINK` at runtime:
```bash
docker run -e MODEL_DOWNLOAD_LINK="https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/kusal/medium/en_US-kusal-medium.onnx?download=true" \
           -p 5000:5000 piper
```
Browse available voices: <https://huggingface.co/rhasspy/piper-voices>

## Client Usage
```bash
# Simple curl – save WAV
curl "http://localhost:5000/?text=Hello+World" -o hello.wav

# Python client (requires: pip install requests)
# Plays audio via pw-play / paplay / mpv / ffplay – no extra Python audio lib needed
python client/piper-tts.py "Hello World"
python client/piper-tts.py "Hello World" "http://localhost:5000"
```

## Development Notes
- The project depends on **piper** being cloned at build time (`/app/piper`).  
  If piper's repository structure changes, the `WORKDIR` and `pip install` paths in the Dockerfile may need updating.
- `download-model.py` always saves files as `model.onnx` / `model.onnx.json` – only one model is active at a time.
- The HTTP server is provided by `piper`'s optional `http_server` extra; it listens on `0.0.0.0:5000` by default.
- To persist the downloaded model across container restarts, mount a volume: `-v /host/models:/app/models`.
