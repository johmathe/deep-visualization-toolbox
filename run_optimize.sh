#!/bin/bash
docker build -t vis .
nvidia-docker run -it --rm -v /home/johmathe/:/home/johmathe/ vis  python optimize_image.py --lr-params '{"lr": 100.0}' $*
