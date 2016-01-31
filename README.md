#checkheaders
A small script to check if HSTS headers and headers to protect against clikjacking attacks are implemented.
In addition to it
1.  Check the SSL configuration of the website using "SSLScan" and store the output to default filename or filename mentioned by the user.
2.  Check if insecure HTTP methods are enabled in the server.
3.  Check if the repsonse headers disclose any server information.

usage: checkheaders.py [-h] [-u URL] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     enter the webaddress Ex: https://example.com
  -o OUTPUT, --output OUTPUT
                          enter a filename for sslscan output
Dependecies:
The application depends on 
1.  [Curl](http://curl.haxx.se/).
2.  SSLscan.
3.  [requests](http://docs.python-requests.org/en/latest/).

* To-Do
Need to add a function to check if an application has a port 80/443 open when given a url