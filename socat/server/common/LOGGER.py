# -*- coding: utf-8 -*-
import logging
import os.path
import time

from common import CONSTANT

infologger = logging.getLogger()
infologger.setLevel(CONSTANT.LOG_LEVEL)
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
log_path = os.path.dirname(os.getcwd()) + '/Logs/'
log_name = CONSTANT.LOG_NAME
logfile = log_name
fh = logging.FileHandler(logfile, mode='a', encoding='utf-8')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "%(asctime)s - %(filename)-20s[line:%(lineno)-6s] - %(levelname)-8s %(threadName)-30s: %(message)s")
fh.setFormatter(formatter)
infologger.addHandler(fh)


def getlogger():
    return infologger
