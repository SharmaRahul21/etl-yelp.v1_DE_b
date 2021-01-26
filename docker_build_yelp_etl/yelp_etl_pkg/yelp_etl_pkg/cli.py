import os
import sys
import datetime as t
import pandas as pd
import json
import numpy as np
import sqlite3

import Xtract_data as Xtract_data
import Xform_dataStructs as Xform_dataStructs
import helper as helper

if __name__ == '__main__':

    print("******** Creating an instance of helper.loadConfigProps to load variables from Config file ********")
    configFilePath = "../data/Yelp_data_Set/config.properties"
    config = helper.loadConfigProps(configFilePath)

    print("******** Creating an instance of helper.initializeLogger for logging ********")
    log_dir = config['S3_PATH_INFO']['LOGGING_PATH']
    logger = helper.initializeLogger(log_dir, app_name = '[Yelp_DE_Excercise]',slogger=True)
    
    # Extracting Data
    print("******** Extracting Data ********")
    logger.info('Capturing Yelp Dataset path from Config File')
    data_path = config['S3_PATH_INFO']['DATA_PATH']

    logger.info('Creating an instance of Xtract_data.extract_data and extracting data from CSV, JSON and SQLITE3')
    df_users, df_r, df_business_ctr, df_ba = Xtract_data.extract_data(data_path)
    
    print("******** Transforming and Loading Datasets ********")
    
    # Q1 - Creating Summarized Data Set and Writing to S3
    print("******** Computing Q1 ********")
    logger.info('Joining Datasets to create a Summarized View')
    df_f = Xtract_data.create_base_ds(df_users, df_r, df_business_ctr, df_ba)
    logger.info('Writing Summarized View, Q1 to Docker Container')
    #path_to_write_q1 = config['S3_PATH_INFO']['PATH_TO_WRITE_Q1']
    path_to_write_q1_docker = "../data/cli_dkr_output/q1_op.csv" # As S3 API has issues with anonymous users uploadiing data using multipart for larger than 100 mb data
    Xtract_data.write_as_csv(df_f, path_to_write_q1_docker)

    # Q2 - Performing computation and Writing to S3
    print("******** Computing Q2 data: ********")
    logger.info('Transforming Dataset to calculate Q1 - Mean reviews by zipcode')
    df_q2f = Xform_dataStructs.transform_q2(df_f)
    logger.info('Writing Q2 Transformed View to Docker Container')
    #path_to_write_q2 = config['S3_PATH_INFO']['PATH_TO_WRITE_Q2']
    path_to_write_q2_docker = "../data/cli_dkr_output/q2_op.csv"
    Xtract_data.write_as_csv(df_q2f, path_to_write_q2_docker)
    
    # Q3 - Performing computation and Writing to S3
    print("******** Computing Q3 data: ********")
    logger.info('Transforming Dataset to calculate Q2 - Mean reviews by zipcode for top 5 business dense zips')
    df_q3f = Xform_dataStructs.transform_q3(df_f)
    logger.info('Writing Q3 Transformed View to Docker Container')
    #path_to_write_q3 = config['S3_PATH_INFO']['PATH_TO_WRITE_Q3']
    path_to_write_q3_docker = "../data/cli_dkr_output/q3_op.csv"
    Xtract_data.write_as_csv(df_q3f, path_to_write_q3_docker)
    
    # Q4 - Performing computation and Writing to S3
    print("******** Computing Q4 data: ********")
    logger.info('Transforming Dataset to calculate Q3 - Top 10 most active reviewers')
    df_q4f = Xform_dataStructs.transform_q4(df_f)
    logger.info('Writing Q4 Transformed View to Docker Container')
    #path_to_write_q4 = config['S3_PATH_INFO']['PATH_TO_WRITE_Q4']
    path_to_write_q4_docker = "../data/cli_dkr_output/q4_op.csv"
    Xtract_data.write_as_csv(df_q4f, path_to_write_q4_docker)
