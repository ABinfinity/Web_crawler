from urllib.parse import urlparse

#get domain name (example.com)

def get_domain_name(url):
	try:
		results = get_sub_domain_name(url).split(".")
		return results[-2] + "." + results[-1]
	except Exception as e:
		raise ""






# get sub domain name (name.example.com)

def get_sub_domain_name(url):
	try:
		return urlparse(url).netloc #return network location
	except Exception as e:
		return ""



