#!/usr/bin/env python3

from setuptools import setup

# this will not work yet

setup(
    author = None,
    keywords = "python cli utility",
    name = None,
    version = None,
    description = None,
    long_description = None,
    long_description_content_type = None,
    url = None,
    py_modules = [ None ],
    package_dir = { '' : 'src' },
    install_requires = [
        'click',
        'colorama',
        'pathlib'
    ],
    python_version=">=3.6",
    classifiers = [
        "Natural Language :: English",
        "Natural Language :: Japanese",
        "Natural Language :: German",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
        "Development Status :: 1 - Planning",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU Public License v3 (GPLv3)"
    ]
)
