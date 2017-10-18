# Author: Antionette Hayward
# Course: TCMG 476
# Date: 10/16/2017
# This python program will check a log file (https://s3.amazonaws.com/tcmg412-fall2016/http_access_log) and answer certain questions 

import urllib2
import re
import sys
from datetime import datetime

remote_url = 'https://s3.amazonaws.com/tcmg412-fall2016/http_access_log'
local_file = 'http_access_log.dms'
log_path = 'logs/'


print "\Downloading log file from url..."
response = urllib2.urlopen(remote_url)
with open(local_file, "wb") as local:
	local.write(response.read())
print "File retrieved and saved (%s) \n\n" % local_file



f = open("http_access_log.dms", "r")
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
if(input == 1):
    st= total_requests " requests were made in the time period."
  elif (input == 2):
  	st= requests 
  elif (input == 3):
  	st= 4xx_status
  elif (input == 4):
  	st= 3xx_status
  elif (input == 5):
  	st= most_requested
  elif (input == 6):
  	st= least_requested
  elif (input == 7):
  	st= total_requests " requests were made in the time period.", requests, 4xx_status, 3xx_status, most_requested, least_requested				

 print st	
