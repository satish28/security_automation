"""
Module to perform SSLscan for a URL, check HSTS
, clickjacking headers & check server version
& check HTTP methods using options.
"""
import argparse
import sys
import re
from security_tests.clickjacking_headers import check_clickjacking
from security_tests.hsts_headers import check_hsts
from security_tests.httpmethods import check_httpmethods
from security_tests.serverversion_info import info_disclosure
from security_tests.sslscan import sslscan

# run the checks
def run_checks(url, sslscan_filename):
    """
    Helper function to run the checks
    """
    check_clickjacking(url)
    check_hsts(url)
    sslscan(url, sslscan_filename)
    info_disclosure(url)
    check_httpmethods(url)

#main function
def main():
    """
    Getting arguments from the user
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url",\
                        help="enter the webaddress Ex: https://example.com")
    parser.add_argument("-o", "--output",\
                        help="enter a filename for sslscan output")
    args = parser.parse_args()
    if args.url is None:
        parser.print_help()
        sys.exit(1)
    else:
        url = args.url
        if re.match(r'^(http|https)://', url):
            if args.output is None:
                print "The output of SSLScan will be stored as sslscan"
                sslscan_filename = "sslscan"
                run_checks(url, sslscan_filename)
            else:
                sslscan_filename = args.output
                run_checks(url, sslscan_filename)
        else:
            print "Check usage for the url"
            parser.print_help()

if __name__ == '__main__':
    main()
