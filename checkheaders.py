#!/usr/bin/python

import requests,argparse,sys

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--URL', help='Put your URL here', required=False)
parser.add_argument('-f', '--file', help='What file?', required=False)
parser.add_argument('-d', '--debug', '-v', '--verbose', help='Be a bit more verbose', required=False)
args = parser.parse_args()

#if args.debug:
#	print args.URL
#	print args.file
#


if not args.URL:
	for url in open("sites.txt"):
	    try:
	        r = requests.head(url.rstrip(), allow_redirects=True)
		print r.headers

		print "------------------------------------------"
		print "Site Headers Being Checked:", url
	        if 'Strict-Transport-Security' in r.headers:
	                print "Strict-Transport-Security:", r.headers['Strict-Transport-Security']
	        else:
	                print "Strict-Transport-Security Not Present"
		if 'X-XSS-Protection' in r.headers:
			print "X-XSS-Protection:", r.headers['X-XSS-Protection']
		else: 
			print "X-XSS-Protection Not Present"
	        if 'X-Content-Type-Options' in r.headers:
	                print "X-Content-Type-Options:", r.headers['X-Content-Type-Options']
	        else: 
	                print "X-Content-Type-Options Not Present"
		if 'X-Frame-Options' in r.headers:
			print "X-Frame-Options:", r.headers['X-Frame-Options']
		else:
			print "X-Frame-Options Not Present"
	        if 'Content-Security-Policy' in r.headers:
	                print "Content-Security-Policy:", r.headers['Content-Security-Policy']
	        else: 
	                print "Content-Security-Policy Not Present"
		if 'Public-Key-Pins' in r.headers:
			print "Public-Key-Pins:", r.headers['Public-Key-Pins']
		else:
			print "Public-Key-Pins Not Present"
		print "------------------------------------------","\n"
	  
	    except:
	        print "Unknown Exception:",sys.exc_info()[0]
		raise
else:
	        r = requests.head(args.URL.rstrip())
		print r.headers

                print "------------------------------------------"

                print "Site Headers Being Checked:", args.URL
                if 'Strict-Transport-Security' in r.headers:
                        print "Strict-Transport-Security:", r.headers['Strict-Transport-Security']
                else:
                        print "Strict-Transport-Security Not Present"

                if 'X-XSS-Protection' in r.headers:
                        print "X-XSS-Protection:", r.headers['X-XSS-Protection']
                else:
                        print "X-XSS-Protection Not Present"

                if 'X-Content-Type-Options' in r.headers:
                        print "X-Content-Type-Options:", r.headers['X-Content-Type-Options']
                else:
                        print "X-Content-Type-Options Not Present"

                if 'X-Frame-Options' in r.headers:
                        print "X-Frame-Options:", r.headers['X-Frame-Options']
                else:
                        print "X-Frame-Options Not Present"

                if 'Content-Security-Policy' in r.headers:
                        print "Content-Security-Policy:", r.headers['Content-Security-Policy']
                else:
                        print "Content-Security-Policy Not Present"

                if 'Public-Key-Pins' in r.headers:
                        print "Public-Key-Pins:", r.headers['Public-Key-Pins']
                else:
                        print "Public-Key-Pins Not Present"


                if 'X-Clacks-Overhead' in r.headers:
                        print "X-Clacks-Overhead:", r.headers['X-Clacks-Overhead']
                else:
                        print "X-Clacks-Overhead Not Present"

                print "------------------------------------------","\n"

