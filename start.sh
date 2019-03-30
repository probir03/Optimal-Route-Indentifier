#!/bin/bash

#Activating virtual env
echo "Activating virtual environment"
source venv/bin/activate

#start all the supervisor process
echo "start supervisor programs"
supervisorctl -c supervisord.conf start all
