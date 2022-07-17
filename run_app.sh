#!/bin/bash
if ! [ -x "$(command -v python3)" ]; then
  echo 'Python 3 is not installed.' >&2
  exit 1
fi
python3 app.py