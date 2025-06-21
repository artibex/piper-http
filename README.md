# piper-http
Creates a docker image that runs the piper http service found in this repo:
https://github.com/rhasspy/piper

## How to use this:
1. Download repo via git clone or direct download
2. Navigate to the folder where the Dockerfile is
3. Run `docker build -t piper .` to create the image
4. Use `docker run --name piper -p 5000:5000 -v $(pwd)/models:/app/models piper` to run your own image

If you don't want to build your own image you can also use my image on docker hub (English voice example):
`docker run -e MODEL_DOWNLOAD_LINK=https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/kusal/medium/en_US-kusal-medium.onnx?download=true --name piper -p 5000:5000 -v $(pwd)/models:/app/models artibex/piper-http`

See image on docker hub for more information:
https://hub.docker.com/r/artibex/piper-http

### Support the Developer:
- [Buy Me a Coffee](https://buymeacoffee.com/artibex)
- [My Music / Socials](https://hyperfollow.com/Artibex)
