"""
Check if an app has HSTS header enabled
"""
import requests

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
