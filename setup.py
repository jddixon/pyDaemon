#!/usr/bin/python3
# py_daemon/setup.py

""" distutils setup for py_daemon. """

import re
from distutils.core import setup
__version__ = re.search(r"__version__\s*=\s*'(.*)'",
                        open('py_daemon/__init__.py').read()).group(1)

# see http://docs.python.org/distutils/setupscript.html

setup(name='py_daemon',
      version=__version__,
      author='Jim Dixon',
      author_email='jddixon@gmail.com',
      py_modules=[],
      packages=['py_daemon'],
      # following could be in scripts/ subdir
      scripts=[],
      description='python3 daemonizer',
      url='https://jddixon.github.io/py_daemon',
      classifiers=[
          'Development Status :: 1 - Planning',
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Natural Language :: English',
          'Programming Language :: Python 3',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      )
