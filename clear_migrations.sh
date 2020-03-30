#!/bin/bash

# delete all files in /migrations except __init__.py
find . -path "./datacollector/migrations/*.py" -not -name "__init__.py" -delete

# delete compiled versions of the files
find . -path "./datacollector/migrations/*.pyc" -delete
