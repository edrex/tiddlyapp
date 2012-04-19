#!/usr/bin/env python

from setuptools import setup

install_requires = []

try:
  import argparse
except ImportError:
  install_requires.append('argparse==1.1')

setup(
    name="tiddlyapp",
    version="0.1.0",
    description="Couchapp for tiddlyweb",
    author="Eric Drechsel",
    author_email="ericdrex@gmail.com",
    scripts=["scripts/tiddlyapp"],
    packages=[],
    install_requires=install_requires,
)
