import sys
import random
import time
import logging

logger = logging.getLogger(__name__)

def configure_logging(level=logging.DEBUG):
    rlogger = logging.getLogger()
    rlogger.setLevel(level)

    shandler = logging.StreamHandler(stream=sys.stderr)
    sformatter = logging.Formatter("%(asctime)s %(threadName)s %(levelname)s [%(funcName)s]: %(message)s")
    shandler.setFormatter(sformatter)
    shandler.setLevel(level)
    rlogger.addHandler(shandler)

def runit(name):
    sleep = random.uniform(3, 12)
    logger.debug(f'{name} running - sleeping {sleep:.2f}s')
    time.sleep(sleep)
    logger.info(f'{name} completed')
