import urllib2
import re
from sets import Set

# Author: Robin Duda
# 2015-07-27

SEARCH_DEPTH = 10
SEARCH_DELTA = 10

providers = [
	'https://se.search.yahoo.com/search;?p=%QUERY%&b=%PAGE%', 
	'http://www.bing.com/search?q=%QUERY%&first=%PAGE%'
]

blacklist_word = Set([
	'msn',
	'bing',
	'yahoo',
	'microsoft',
	'duckduck',
	'wikipedia',
	'google'
])

blacklist_url = Set([
	'http://schemas.live.com/',
	'https://s.yimg.com/',
	'https://login.live.com/',
	'http://www.w3.org/',
	'https://www.flickr.com/'
])


def whitelisted(urls):
	""" returns a subset list of the argument with urls not blacklisted. """
	safe = []
	for url in urls:
		blacklisted = False
		for word in blacklist_word:
			if (word in url):
				blacklisted = True

		if not (url in blacklist_url) and not blacklisted:
			safe.append(url)
	return safe


def search_links(queries):
	""" Uses search terms to find links from search providers. """
	urls = Set([])
	regex_links = re.compile('(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))')
	for query in queries:
		try:
			for provider in providers:
				for page in range(0, SEARCH_DEPTH):
					request = urllib2.urlopen(provider.replace('%QUERY%', query).replace('%PAGE%', str(page * SEARCH_DELTA)), timeout=1)
					html = request.read()
					links = regex_links.findall(html)
			
					for link in links:
						urls.add('://'.join(list(link)) + '/')		
		except:
			print('search failed for ' + query)
	return (whitelisted(list(urls)))


def extract_links(sources):
	""" Extracts links on a given page. """
	urls = Set([])
	for source in sources:
		try:
			request = urllib2.urlopen(source, timeout=1)
			html = request.read()
			p = re.compile('(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))')
			links = p.findall(html)
			
			for link in links:
				urls.add('://'.join(list(link)) + '/')		
		except:
			print('search failed for ' + query)
	return (whitelisted(list(urls)))

