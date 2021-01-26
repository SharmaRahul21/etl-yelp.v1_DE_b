from datetime import datetime,date,timedelta
import configparser
import io
import os
import logging
import sys

def loadConfigProps(configFilePath):
    config = configparser.RawConfigParser()
    config.read(configFilePath)
    return config

def initializeLogger(log_dir, app_name = '[Yelp_DE_Excercise]',slogger=True):    
    logger = logging.getLogger(app_name)
    logger.setLevel(logging.INFO)
    lsh = logging.StreamHandler(sys.stdout)    
    lsh.setLevel(logging.INFO)    
    lformat = logging.Formatter(fmt='%(asctime)s.%(msecs)03d %(name)s '+app_name+' %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S')
    lsh.setFormatter(lformat)    
    logger.addHandler(lsh)
    if (slogger):
        lfh = logging.FileHandler(log_dir+app_name+".log")
        lfh.setLevel(logging.INFO)
        lfh.setFormatter(lformat)
        logger.addHandler(lfh)
    return logger