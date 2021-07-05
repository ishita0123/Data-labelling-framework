
Spam Detection using Snorkel Labeling function

Python: 3.8
Snorkel 0.9.7

Clone the repository and install the packages using pip install -r requirements.txt
and run the following cmd on terminal after you cd to the spam folder: python spam.py

You will see a file named output.csv in the folder.


Steps to make a docker containers:
1. cd to the folder containing spam.py
2. In terminal, write the following command:  docker build -t spam1 .
 (This will build the docker image).
 
 3. To run this image: docker run spam1 
 
 
