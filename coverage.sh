#!/bin/bash

#activating virtual environment
# echo "activating virtual environment"
# source venv/bin/activate

#running coverage command

echo "running test..."
coverage run manage.py test measure_builder.test

#genrating coverage html folder
echo "genrating coverage report...!"
coverage html