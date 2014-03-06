import multiprocessing
import os

repository_name = 'sepsidae_site'

bind = "127.0.0.1:8000"
timeout = 120
pidfile = os.path.dirname(__file__) + "process.pid"
workers = multiprocessing.cpu_count() * 2 + 1
accesslog = "/var/log/gunicorn/{}.log".format(repository_name)
errorlog = "/var/log/gunicorn/{}.error.log".format(repository_name)
loglevel = 'warning'
