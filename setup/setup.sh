#!/bin/bash

#installing virtual env
echo "installing virtual environment"
virtualenv -p python3 venv

#activating virtual environment
echo "activating virtual environment"
source venv/bin/activate

#Installing dependencies  .
#....
echo "Installing dependencies"
pip3 install -r setup/requirements.txt

mkdir supervisor
#Run supervsior to listening on a port that one of our HTTP servers is configured
supervisord