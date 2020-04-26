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

def copy_settings(filename, project_name, overwrite = False):
    target_file= path_settings(project_name).joinpath(filename)

    if not target_file.exists() or (target_file.exists and overwrite):
        shutil.copy(
            Path.cwd().joinpath('src').joinpath(filename),
            target_file
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

def kelvin_to_celsius(kelvin_temp):
    return kelvin_temp - 273.15

def fahrenheit_to_celsius(fahrenheit_temp):
    return (fahrenheit_temp - 32) * 5/9

def set_temp_string(temperature, unit):
    if unit == 'celsius':
        return "{:05.2F}{}C".format(temperature, u'\N{DEGREE SIGN}')
    elif unit == 'kelvin':
        return "{:06.2F}K".format(temperature)
    elif unit == 'fahrenheit':
        return "{:06.2F}{}F".format(temperature, u'\N{DEGREE SIGN}')

def color_temperature(temperature, temp_string, unit):
    init()
    # temporarily convert to celsius so the all comparisons can be
    # applied for all temperature regardless of their unit
    if unit == 'kelvin':
        temperature = kelvin_to_celsius(temperature)
    elif unit == 'fahrenheit':
        temperature = fahrenheit_to_celsius(temperature)

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
