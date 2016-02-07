#Security Automation
Use this package to perform a basic security checks on a web application.
The applications performs the following<br />
1. Checks if the application has Clickjacking protection headers <br />
2. Checks if the application has HSTS implemented <br />
3. Performs a SSLScan and outputs the allowed ciphers for the application <br />
4. Checks what HTTP methods are enabled on the server <br />
5.  Checks if the server version information is revealed in response headers <br />

##SetUp
Use python setup.py install to install the application

##Dependecies:
The application depends on <br />
1. [Curl](http://curl.haxx.se/)<br />
2. SSLscan <br />
3. [requests](http://docs.python-requests.org/en/latest/) <br />

##Usage
security_automation [-h] [-u URL] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit <br />
  -u URL, --url <<url>>     enter the webaddress Ex: https://example.com <br />
  -o OUTPUT, --output <<filename>>   enter a filename for sslscan output <br />
<br />


##To-Do<br />
Need to add a function to check if an application has a port 80/443 open when given a url