#coding=utf-8

from json_log_demo import setup_logging
import logging
import os


logger = logging.getLogger(__name__)
setup_logging()

def saysomething():
	logger.info("info!")
	logger.warn("warn")
	logger.error("error")
	logger.debug("debug")
	logger.warning("343443")

if __name__ == '__main__':
	saysomething()