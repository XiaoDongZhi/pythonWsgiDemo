#!/usr/bin/python

def application(environ, start_response):
    ctype = "text/html"
    response_body = ""
    if environ["PATH_INFO"] == "/" or environ["PATH_INFO"] == "/hello":
        response_body = "Hello, world"
    elif environ["PATH_INFO"] == "/goodbye":
        response_body = "Ok see ya"
    status = "200 OK"
    response_headers = [('Content-Type', ctype), ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]