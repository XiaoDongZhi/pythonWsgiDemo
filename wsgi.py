import sys
import os
import json

# set the right path for the demo import
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)
from demo import inventory


def application(environ, start_response):
    ctype = 'application/json'
    response_body = ""

    if environ["PATH_INFO"] == "/" or environ["PATH_INFO"] == "":
        cur_inventory = inventory.list_inventory()
        item_count = 0
        for item in cur_inventory:
            if item_count > 0:
                response_body += ","
            response_body = response_body + item.to_json()
            item_count += 1
        response_body = "[" + response_body + "]"
    elif environ["PATH_INFO"] == "/order":
        #should handle a post here and... you know... parameters
        response_body = json.dumps({"order": 2343214})

    status = "200 OK"
    response_headers = [("Content-Type", ctype), ("Content-Length", str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]
