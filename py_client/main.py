"""
Usage:
    python main.py post_auth AZURE_FUNCTION_SECRET1
 """

__author__  = 'Chris Joakim'
__license__ = "MIT"
__version__ = "August 2021"

import json
import os
import pprint
import sys
import time
import uuid

import arrow
import requests
import jinja2

from docopt import docopt
from operator import itemgetter


def post_auth(secret_env_var):
    print('post_auth, secret_env_var: {}'.format(secret_env_var))

    secret = os.environ[secret_env_var]
    url    = os.environ['AZURE_FUNCTION_URL']
    

    print('secret: {}'.format(secret))
    print('url:    {}'.format(url))

    data = dict()
    data['auth'] = secret
    data['name'] = 'miles'

    resp = invoke('post', url, {}, data)

def invoke(method, url, headers={}, json_body={}):
    # This is a generic method which invokes all HTTP Requests to the QnA Service
    print('===')
    print("invoke: {}\nurl: {}\nheaders: {}\nbody: {}".format(method.upper(), url, headers, json_body))
    print('---')
    if method == 'get':
        r = requests.get(url=url, headers=headers)
    elif method == 'post':
        r = requests.post(url=url, headers=headers, json=json_body)
    elif method == 'put':
        r = requests.put(url=url, headers=headers, json=json_body)
    elif method == 'patch':
        r = requests.patch(url=url, headers=headers, json=json_body)
    elif method == 'delete':
        r = requests.delete(url=url, headers=headers)
    else:
        print('error; unexpected method value passed to invoke: {}'.format(method))

    print('response: {}'.format(r))
    if r.status_code < 300:
        try:
            resp_obj = json.loads(r.text)
            outfile = 'tmp/{}.json'.format(time.time())
            write_obj_as_json_file(resp_obj, outfile)
        except Exception as e:
            print("exception processing http response".format(e))
            print(r.text)
    else:
        print(r.text)

    print(str(type(r)))  # r is an instance of <class 'requests.models.Response'>
    return r  

def print_http_response(resp):
    try:
        print(resp)
        print(resp.text)
    except:
        pass

def load_json_file(infile):
    with open(infile) as json_file:
        return json.load(json_file)

def write_obj_as_json_file(outfile, obj, sort_keys=False):
    txt = json.dumps(obj, sort_keys=False, indent=2)
    with open(outfile, 'wt') as f:
        f.write(txt)
    print("file written: " + outfile)

def write(outfile, s, verbose=True):
    with open(outfile, 'w') as f:
        f.write(s)
        if verbose:
            print('file written: {}'.format(outfile))

def print_options(msg):
    print(msg)
    arguments = docopt(__doc__, version=__version__)
    print(arguments)


if __name__ == "__main__":

    if len(sys.argv) > 1:
        func = sys.argv[1].lower()

        if func == 'post_auth':
            env_var = sys.argv[2]
            post_auth(env_var)

        elif func == 'xxx':
            pass

        else:
            print_options('Error: invalid function: {}'.format(func))
    else:
            print_options('Error: no command-line args entered')
