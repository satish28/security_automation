"""
Perform sslscan and print all allowed ciphers to a file
"""
import subprocess
import re

def sslscan(url, output_file):
    """
    Perform SSLscan for the given url and output it to the given file
    """
    if re.match(r'^https://', url):
        scan_url = re.findall(r'^https://(.*?)(?=.com)', url)[0] + ".com"
        subprocess.check_output(["sslscan", "--no-failed", "--renegotiation",\
                                 "--xml=%s" %output_file, scan_url])
    else:
        print "Are you sure the application use https??, if so add the url as https://example.com"

