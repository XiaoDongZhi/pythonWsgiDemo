#!/usr/bin/python

from demo import controller
import json


def application(environ, start_response):
    ctype = "application/json"
    response_body = ""

    if environ["PATH_INFO"] == "/" or environ["PATH_INFO"] == "/inventory":
        inventory = controller.list_inventory()
        response_body = json.dumps(inventory)

    elif environ["PATH_INFO"] == "/goodbye":
        response_body = "Ok see ya"

    status = "200 OK"
    response_headers = [('Content-Type', ctype), ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]