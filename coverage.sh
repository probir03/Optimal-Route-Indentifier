#!/bin/bash
#running coverage command

echo "running test..."
coverage run manage.py test grids.test

#genrating coverage html folder
echo "genrating coverage report...!"
coverage html