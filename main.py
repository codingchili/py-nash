import sys
import os
import modloader
import crawler

# Author: Robin Duda
# 2015-07-27

class colors:
    LINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'


def menu():
	""" Print the menu. """
	print(colors.BLUE + '\n--------------- PyNash - v0.1 ---------------')
	print('search <query..> find links in a search provider query.')
	print('scan <url..> scan the given link for vulnerabilities.')
	print('links <url..> extract links from given urls.')
	print('exit - closes the application.')


def run(links):
	""" Executes test on all of the links. """
	for link in links:
		print(colors.LINK + link),

		for index in range(0, modloader.count()):
			if (modloader.scan(index, link)):
				print(colors.GREEN + ' ' + modloader.tag(index) + ' ' + colors.BLUE)
			else:
				print('')


def call(function, argument):
	""" Call the testing modules. """
	if (function == 'search'):
		print('Gathering links..')
		run(crawler.search_links(argument))
		return True
	elif (function == 'scan'):
		run(argument)
		return True
	elif (function == 'links'):
		print('\n'.join(crawler.extract_links(argument)))
		return True
	else:
		return False


def interface():
	""" Main script loop. """
	menu()
	while (True):
		option = raw_input(colors.BLUE + '# ')
		print("\n")
		function = option.split(' ')[0]
		argument = option.split(' ')
		argument.pop(0)

		if call(function, argument):
			print(colors.GREEN + '\n-- completed. --\n')
		elif (function == 'exit'):
			break
		else:
			continue

# Get any command line parameters.

modloader.load()

if len(sys.argv) > 1:
	arguments = sys.argv
	arguments.pop(0)
	function = arguments.pop(0)
	if (call(function, arguments) == False):
		menu()
else:
	interface()

