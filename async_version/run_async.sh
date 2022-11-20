#!/bin/bash
set -e
/usr/local/bin/gunicorn -b '0.0.0.0:8001' --workers 1 --backlog 0 -k uvicorn.workers.UvicornWorker 'web_async:app'