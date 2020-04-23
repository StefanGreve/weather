#!/usr/bin/env python3

import os
import json
import shutil
from platform import system

from colorama import init, Fore, Style
from pathlib import WindowsPath, PosixPath, Path

def read_file(file):
    with open(file, encoding = 'utf-8', mode = 'r') as io:
        return io.read()

def read_json(file):
    return json.loads(read_file(file))

def path_settings(directory):
    dest = os.getcwd()

    if system() == 'Windows':
        appdata = WindowsPath(os.getenv('APPDATA'))
        dest = appdata.joinpath(directory)
    else:
        dest = PosixPath('/etc').joinpath(directory)

    dest.mkdir(parents = True, exist_ok = True)

    return dest

def copy_settings(filename, project_name):
    shutil.copy(
        Path.cwd().joinpath('src').joinpath(filename), 
        path_settings(project_name).joinpath(filename)
    )

def status_to_emoji(status):
    if status == 'Clear':
        return "☀️"
    elif status == 'Clouds':
        return '☁️'
    elif status == 'Sun':
        return '🌤️'
    elif status == 'Fog':
        return '🌫'
    elif status == 'Snow':
        return '❄️'
    else:
        raise NotImplementedError()

def color_temperature(temperature, temp_string):
    init()
    if temperature < 0:
        return f"{Style.DIM}{Fore.CYAN}{temp_string}{Style.RESET_ALL}"
    elif temperature < 5:
        return f"{Style.NORMAL}{Fore.CYAN}{temp_string}{Style.RESET_ALL}"   
    elif temperature < 10:
        return f"{Style.BRIGHT}{Fore.CYAN}{temp_string}{Style.RESET_ALL}"
    elif temperature < 15:
        return f"{Style.DIM}{Fore.YELLOW}{temp_string}{Style.RESET_ALL}"
    elif temperature < 20:
        return f"{Style.NORMAL}{Fore.YELLOW}{temp_string}{Style.RESET_ALL}"
    elif temperature < 25:
        return f"{Style.BRIGHT}{Fore.YELLOW}{temp_string}{Style.RESET_ALL}"
    elif temperature < 30:
        return f"{Style.DIM}{Fore.RED}{temp_string}{Style.RESET_ALL}"
    elif temperature < 35:
        return f"{Style.NORMAL}{Fore.RED}{temp_string}{Style.RESET_ALL}"
    else:
        return f"{Style.BRIGHT}{Fore.RED}{temp_string}{Style.RESET_ALL}"



