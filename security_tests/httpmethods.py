"""
Check HTTP methods enabled in the server
"""
import requests
import subprocess
import re

#check http methods
def check_options(url):
    """
    Use curl to check if OPTIONS HTTP methods are implemented
    """
    check_options = requests.options(url, verify=False)
    if check_options.status_code == 200:
        print "Options are enabled %s", check_options.status_code
    else:
        print "Options not enabled. %s", check_options.status_code


#check Trace method
def check_trace(url):
    """
    Use subprocess and curl to check if TRACE method is enabled
    """
    check_trace = subprocess.Popen('curl --insecure -I -s -L -X TRACE %s' %url,\
                                   stdout=subprocess.PIPE, shell=True)
    check_trace_grep = subprocess.Popen(["grep", "HTTP/1.1"],\
                                        stdin=check_trace.stdout, stdout=subprocess.PIPE)
    check_trace.stdout.close()
    check_trace_status = check_trace_grep.communicate()
    trace_status = re.findall(r'\d{3}', check_trace_status[0])
    if int(trace_status[0]) >= 200 and int(trace_status[0]) < 300:
        print "TRACE method is enabled on the server"
    else:
        print "TRACE method is not enabled on the server.\
        Response status code = %s", trace_status[0]

#check Track method
def check_track(url):
    """
    Use subprocess and curl to check if TRACK method is enabled
    """
    check_track = subprocess.Popen('curl --insecure -I -s -L -X TRACK %s' %url,\
                                   stdout=subprocess.PIPE, shell=True)
    check_track_grep = subprocess.Popen(["grep", "HTTP/1.1"],\
                                        stdin=check_track.stdout, stdout=subprocess.PIPE)
    check_track.stdout.close()
    check_track_status = check_track_grep.communicate()
    track_status = re.findall(r'\d{3}', check_track_status[0])
    if int(track_status[0]) >= 200 and int(track_status[0]) < 300:
        print "TRACK method is enabled on the server"
    else:
        print "TRACK method is not enabled on the server.\
        Response status code = %s", track_status[0]

def check_httpmethods(url):
    """
    Check the server for insecure http methods
    """
    check_options(url)
    check_trace(url)
    check_track(url)
