#!/usr/bin/env python3

from setuptools import setup
from src import utils

#region pre-setup procedures

META, SETTINGS, PROJECT = "meta.json", "settings.json", "weather"

utils.copy_settings(META, PROJECT)
utils.copy_settings(SETTINGS, PROJECT)

METADATA = utils.read_json(utils.path_settings(PROJECT).joinpath(META))

#endregion

setup(
    author = METADATA['author'],
    author_email = METADATA['author_email'],
    keywords = "python cli utility weather",
    name = METADATA['name'],
    version = METADATA['version'],
    description = METADATA['description'],
    long_description = utils.read_file("README.md"),
    long_description_content_type = "text/markdown",
    url = METADATA['url'],
    py_modules = [ PROJECT ],
    package_dir = { '' : 'src' },
    install_requires = [
        'click',
        'colorama',
        'pyowm'
    ],
    python_version=">=3.6",
    classifiers = [
        "Natural Language :: English",
        "Natural Language :: Japanese",
        "Natural Language :: German",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU Public License v3 (GPLv3)"
    ]
)
