# Author: Robin Duda
# 2015-08-29

"""
  Description of the vulnerability the module tests for.
"""

def tag():
	""" Returns the identifier name for the vulnerability. """
	return "[identifier_name]"

def scan(url):
	""" Perform the scan of a host given by url, returns true if
	vulnerable and false if not. "
	success = False
	try:
		# probe the server and set to Success if vulnerable.
		# write logs/data to fiĺes in ./../drop/identifier_name
	except:
		# catch any exceptions at this level
		pass
	return success
