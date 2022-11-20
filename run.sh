#!/bin/bash
set -e
/usr/local/bin/gunicorn -b '0.0.0.0' --workers 1 --backlog 0 'web:app'