#!/usr/bin/env python3

import os
import json

def read_file(file):
    with open(file, encoding = 'utf-8', mode = 'r') as io:
        return io.read()

def get_key():
    return json.loads(read_file('settings.json'))['API_KEY']
