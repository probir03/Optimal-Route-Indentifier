#!/bin/bash

#Activating virtual env
source venv/bin/activate

#start all the supervisor process
echo "stopping all superviosr programs"
supervisorctl -c supervisord.conf stop all

