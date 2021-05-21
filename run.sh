#!/bin/bash

set -e

gunicorn -b 0.0.0.0:8080 main:app  --reload --workers 4  --max-requests-jitter 200 --max-requests 150