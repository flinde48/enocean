#!/usr/bin/env python
import sys
import subprocess

try:
    from setuptools import setup, find_packages
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "setuptools"])
    from setuptools import setup, find_packages

# Default to 'install' if no command is provided
if len(sys.argv) <= 1:
    sys.argv.append('install')

setup(
    name='enocean',
    version='0.60.1',
    description='EnOcean serial protocol implementation',
    author='Kimmo Huoman',
    author_email='kipenroskaposti@gmail.com',
    url='https://github.com/kipe/enocean',
    packages=[
        'enocean',
        'enocean.protocol',
        'enocean.communicators',
    ],
    scripts=[
        'examples/enocean_example.py',
    ],
    package_data={
        '': ['EEP.xml']
    },
    install_requires=[
        'pyserial>=3.0',
        'beautifulsoup4>=4.3.2',
    ],
    # Removing 'test_suite' or other legacy keys prevents AttributeError in Python 3.13
    zip_safe = False
)
