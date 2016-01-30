import requests

#checking if the app is vulnerable to clickjacking
def check_clickjacking(url):
    response = requests.get(url, verify=False)
    try:
        response_check_clickjacking = response.headers['x-frame-options']
        if response_check_clickjacking == "DENY" or \
        response_check_clickjacking == "SAMEORIGIN":
            print "The app is not vulnerable to clickjacking"
        else:
            print response_check_clickjacking
    except KeyError:
        print "The app is vulnerable to clickjacking"

#checking is HSTS is implemented
def check_hsts(url):
    response = requests.get(url, verify=False)
    try:
        response_check_hsts = response.headers['strict-transport-security']
        if response_check_hsts:
            print "The app has hsts implemented"
    except KeyError:
        print "The app doesn't have HSTS headers"

#perform sslscan for the url using sslscan and output it to a file.
def sslscan(url, output_file):
    pass

#check if server version is disclosed in headers
def info_disclosure(url):
    pass
