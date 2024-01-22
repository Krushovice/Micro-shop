#!/usr/bin/env bash
# exit on error
set -o errexit
python3 -m pip install --upgrade pip
python3 -m pip install poetry
rm poetry.lock
poetry lock
poetry install
