#!/usr/bin/env python3

import os

import utils

import click
from pathlib import Path

def cli():
    click.echo("Hello World from CLI!")
    click.echo(f"Test: {utils.get_key()}")

if __name__ == '__main__':
    cli()
