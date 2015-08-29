import os
import imp
import glob

# Author Robin Duda
# 2015-08-29

modules = []

def load():
	""" Loads all the modules in /modules into an array. """
	print('\nLoaded..')
	for path in glob.glob('./modules/*.py'):
		name, ext = os.path.splitext(os.path.basename(path))
		modules.append(imp.load_source(name, path))
		print(path)


def count():
	""" Return the number of modules loaded. """
	return len(modules)


def tag(index):
	""" Returns the short name of the module. """
	return modules[index].tag()


def scan(index, link):
	""" Returns true if the module detected a vulnerability. """
	return modules[index].scan(link)		
