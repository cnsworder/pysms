#!/usr/bin/env python
# coding=utf-8

from distutils.core import setup

setup(
    name = "pysms",
    version = "0.1",
    description = "simple single message base of udp",
    long_description = open('README.rst').read()
    author = "cnsworder",
    author_email = "cnsworder@gmail.com",
    packages = ["pysms"],
    install_requires = ['pyyaml'],
)
