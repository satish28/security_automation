"""
Check if clickjacking headers are present and display the header value
"""
import requests

def check_clickjacking(url):
    """
    check if x-frame-options headers are implemented
    """
    response = requests.get(url, verify=False)
    try:
        response_check_clickjacking = response.headers['x-frame-options']
        if response_check_clickjacking == "DENY" or \
        response_check_clickjacking == "SAMEORIGIN":
            print "The app is not vulnerable to clickjacking and the value of the header is %s"\
                , response_check_clickjacking
        else:
            print response_check_clickjacking
    except KeyError:
        print "The app is vulnerable to clickjacking"
