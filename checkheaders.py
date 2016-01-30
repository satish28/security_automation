"""
Module to perform SSLscan for a URL, check HSTS
, clickjacking headers & check server version
& check HTTP methods using options.
"""
import requests
import subprocess


def check_clickjacking(url):
    """
    check if x-frame-options headers are implemented
    """
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
    """
    check if  HSTS headers are implemented
    """
    response = requests.get(url, verify=False)
    try:
        response_check_hsts = response.headers['strict-transport-security']
        if response_check_hsts:
            print "The app has hsts implemented"
    except KeyError:
        print "The app doesn't have HSTS headers"

#perform sslscan for the url using sslscan and output it to a file.
def sslscan(url, output_file):
    """
    Perform SSLscan for the given url and output it to the given file
    """
    subprocess.call(["sslscan", "--no-failed", "--renegotiation",\
                     "--xml=%s" %output_file, url])

#check if server version is disclosed in headers
def info_disclosure(url):
    """
    Read the server headers and check if server version is disclosed
    """
    response = requests.get(url, verify=False)
    try:
        response_check_server_version = \
                                        response.headers['server']
        if response_check_server_version:
            print "The server version disclosed is",\
                response_check_server_version
    except KeyError:
        print "The repsonse headers are", response.headers

#check http methods
def check_httpoptions(url):
    """
    Use curl to check if TRACE and TRACK HTTP methods are implemented
    """
    check_options = requests.options(url, verify=False)
    if check_options.status_code == 200:
        print "Options are enabled %s", check_options.status_code
    else:
        print "Options not enabled. %s", check_options.status_code
