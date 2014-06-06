#!/usr/bin/python

# no matter what the environ['PATH_INFO'], just say hello
def application(environ, start_response):
    ctype = "text/html"
    response_body = "Hello, world"
    status = "200 OK"
    response_headers = [('Content-Type', ctype), ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]