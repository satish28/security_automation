"""
Check if the repsonse headers contains any server version information
"""
import requests

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
