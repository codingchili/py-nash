import urllib2
import re

# Author: Robin Duda
# 2015-07-27

"""
	In some cases the .git file might be uploaded to the server
	giving access to the source code. This module checks if a
	.git configuration file exists on the server and attempts to
	read it. In order for the check to complete the server has to
	return a 200 OK for the request and the configuration file
	must begin with the [core] tag. Many servers does not properly
	return a 404 code when a page is missing.
"""

def tag():
	return "[gitfolder]"

def scan(url):
	success = False
	try:
		request = urllib2.urlopen(url + '.git/config', timeout=1)
		if request.getcode() == 200:	
			html = request.read()
			if html.startswith('[core]'):
				success = True
	except:
		pass
	return success
