# About Application:
This is an extract-transform-load application designed in a modularized and reusable format, specifically developed to perform below transformation operations on the Yelp Dataset: 

1. Joins the individual datasets into a base summarized dataset(JSON, CSV and SQLITE3 db)
2. Calculate the mean reviews by business
3. Calculate the mean reviews by zipcode for the Top 5 most business dense zipcodes
4. Calculate the Top 10 most active reviewers


# Overview of the Application: 
The github link () includes a handful of folder and files. And this part of the document intents to describe their purpose. 

1. "yelp_etl_pkg" is the main application package
The packaging of the application is done using dependency manager - Poetry and below is the structure of the it.

yelp_etl_pkg
|-- README.rst
|-- data
|   |-- Yelp_data_Set
|   `-- Yelp_data_Set[Yelp_DE_Excercise].log
|-- dist
|   |-- yelp_etl_pkg-0.1.0-py3-none-any.whl
|   `-- yelp_etl_pkg-0.1.0.tar.gz
|-- poetry.lock
|-- pyproject.toml
|-- tests
|   |-- __init__.py
|   `-- test_yelp_etl_pkg.py
`-- yelp_etl_pkg
    |-- Xform_dataStructs.py
    |-- Xtract_data.py
    |-- __init__.py
    |-- cli.py
    `-- helper.py


2. Folder 'yelp_etl_pkg' inside the package "yelp_etl_pkg" contains the application code modules
	a. Xtract_data.py - This module contains functions that help in extracting the data from sources(JSON, CSV, SQLITE3 placed in 'data.Yelp_data_Set' folder)

	b. Xform_dataStructs.py - This code piece intents to transform the data to create the summarized dataset, and perform computations for Q2,Q3 and Q4 datasets. 

	c. helper.py - This contains functions to implement the config parser (to avoid harcoding in the script and read the paths from config file in real time) and logger object (To enable logging across the application) 

	d. cli.py - This is main.py file which is the driver of the application. 

3. data.Yelp_data_Set[Yelp_DE_Excercise].log - This is the log file where all the logs from run are appended. 

4. tests - This folder contains the test suite to perform testing against the application code. 

5. pyproject.toml - Poetry creates this .toml file which captures the dependencies of the application. 

6. poetry.lock - .lock file contaiins the versions of all dependancies and sub depedancies. 

7. dist - This has the Wheel and tar file of the application which contains all the dependencies and the package modules itself. 


# Running the application
In order to run the application: 
1. pip3 install yelp_etl_pkg-0.1.0-py3-none-any.whl
2. And go to the folder - "yelp_etl_pkg" > 'yelp_etl_pkg' and Run 'python3 cli.py'
3. Refer to folder - data.Yelp_data_Set[Yelp_DE_Excercise].log for checking the logs generated. 
4. This application will perform the advised computations and upload the results to an S3 bucket which can be leveraged using this link - 

In order to run the tests: 
1. Go to the folder "yelp_etl_pkg" and run 'python3.8 -m poetry run pytest tests'


# Deployment of the application
In addition to above, i have created the dockerfile which containerizes the application. For runniing and interacting with the application please use the folder: "". 

1. Go to the folder -docker_build_yelp_etl. This folder contains the dockerfile and the etl application package. 
2. In order to execute it, build the docker image using - docker build -t <image_name eg- myimg> .
3. Run the container using docker run <image_name eg- myimg>
4. You will see the system output and logging statements showing the progress of the application execution. 
5. The dockerized application will output the computation results to a path in docker (PS: S3 was not used here because S3 Uploadfile API intermitenly fails for cases where anonymous users try to upload files larger than 120mb's, which was the case of the CSV Output file for Question 1)
5. In order to copy the output files from docker container: docker container cp <container_name>:/data/cli_dkr_output <path_in_local>

