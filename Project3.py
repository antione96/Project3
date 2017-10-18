# Author: Antionette Hayward
# Course: TCMG 476
# Date: 10/16/2017
# This python program will check a log file (https://s3.amazonaws.com/tcmg412-fall2016/http_access_log) and answer certain questions 

import urllib2
from datetime import date
from datetime import time
from datetime import datetime

def main():
	f = open("http_access_log", "r")
	if f.mode == 'r':
		contents = f.read()
		print contents



# Displays options for you to pick from
print "Which question would you like to know the answer to?";
print "1. How many total requests were made in the time period represented in the log?";
print "2. How many requests were made on each day? per week? per month?";
print "3. What percentage of the requests were not successful (any 4xx status code)?";
print "4. What percentage of the requests were redirected elsewhere (any 3xx codes)?";
print "5. What was the most-requested file?";
print "6. What was the least-requested file?";
print "7. All of the above questions";

#user enters a number for their option

#condition statement to decide which answer to display
