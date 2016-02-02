# securityheadercheck
Command line tool to check the security headers of a website.

Inspired by https://www.securityheaders.io, I just needed a way to quickly check headers for sites in bulk and sites not yet live.

Checks for the presence of the following security headers:

* HSTS - HTTP Strict Transport Security
* CSP - Content Security Policy
* PKP - HTTP Public Key Pinning
* X-Frame-Options
* X-Xss-Protection
* X-Content-Type-Options

## Requirements:

Requires Python and the requests module (http://docs.python-requests.org/en/latest/)

## Usage:

Populate **sites.txt** with the sites you wish to check

Execute the script with:

**./checkheaders.py**
