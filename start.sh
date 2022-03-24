#!/bin/sh

kill $(lsof -t -i:5000)
python index.py