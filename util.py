import config
import logging
import sys
import time


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(config.LOGLEVEL)
    formatter = logging.Formatter(config.LOGFMT, datefmt=config.DATEFMT)
    formatter.converter = time.gmtime
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(config.LOGLEVEL)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.propagate = False
    return logger
