#!/bin/bash
# d: detached
# Mount the project directory to the container for hot-reloading
docker run -p 8000:80 \
  -v /Users/minh/Documents/PythonWorkspace/moderate-api/app:/app \
  -e PYTHONUNBUFFERED=1 \
  --name moderate-api \
  --rm \
  -it \
  moderate-api
