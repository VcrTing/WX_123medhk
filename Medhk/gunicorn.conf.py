import logging
import logging.handlers
from logging.handlers import WatchedFileHandler
import os
import multiprocessing

bind = "0.0.0.0:8091"
backlog = 512 #监听队列数量，64-2048
worker_class = 'sync' # 使用gevent模式，还可以使用sync 模式，默认的是sync模式
workers = multiprocessing.cpu_count()
threads = multiprocessing.cpu_count()*4
loglevel = 'error' # error / info
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'

accesslog = "/root/Medhk/log/gunicorn_access.log"
errorlog = "/root/Medhk/log/gunicorn_error.log" # "路径" 表示日志写入文件，"-" 表示在控制台进行标准输出

proc_name = 'Medhk' # 进程名