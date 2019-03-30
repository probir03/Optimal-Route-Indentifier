import os
import multiprocessing

# bind = 'unix:' + os.getcwd() + '/optimal_route.sock'
bind = "127.0.0.1:8081"
pythonpath = os.getcwd() + '/venv'
chdir = os.getcwd()
workers = multiprocessing.cpu_count() * 2 + 1
