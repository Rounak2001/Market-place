#!/bin/sh
set -e
gunicorn iekart.wsgi --log-file -