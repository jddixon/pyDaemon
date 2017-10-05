#!/usr/bin/python3
# py_daemon/setup.py

""" Setuptools project configuration for py_daemon. """

from os.path import exists
from setuptools import setup

long_desc = None
if exists('README.md'):
    with open('README.md', 'r') as file:
        long_desc = file.read()

setup(name='py_daemon',
      version='0.1.5',
      author='Jim Dixon',
      author_email='jddixon@gmail.com',
      long_description=long_desc,
      packages=['py_daemon'],
      package_dir={'': 'src'},
      py_modules=[],
      include_package_data=False,
      zip_safe=False,
      scripts=[],
      ext_modules=[],
      description='python3 daemonizer',
      url='https://jddixon.github.io/py_daemon',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Natural Language :: English',
          'Programming Language :: Python 2.7',
          'Programming Language :: Python 3.3',
          'Programming Language :: Python 3.4',
          'Programming Language :: Python 3.5',
          'Programming Language :: Python 3.6',
          'Programming Language :: Python 3.7',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],)
