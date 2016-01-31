#checkheaders
A small script to check if HSTS headers and headers to protect against clikjacking attacks are implemented.
In addition to it<br />
1.  Check the SSL configuration of the website using "SSLScan" and store the output to default filename or filename mentioned by the user.<br />
2.  Check if insecure HTTP methods are enabled in the server.<br />
3.  Check if the repsonse headers disclose any server information.<br />

usage: checkheaders.py [-h] [-u URL] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     enter the webaddress Ex: https://example.com
  -o OUTPUT, --output OUTPUT
                          enter a filename for sslscan output
<br />
Dependecies:<br />
The application depends on <br />
1.  [Curl](http://curl.haxx.se/).<br />
2.  SSLscan.<br />
3.  [requests](http://docs.python-requests.org/en/latest/).<br />

* To-Do<br />
Need to add a function to check if an application has a port 80/443 open when given a url