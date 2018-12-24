#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
  name = 'game-assistant',
  version = '0.0.1',
    keywords = ('pip', 'game','assistant'),
    description = 'a game assistant in python',
    long_description = 'a game assistant in python',
    license = 'MIT Licence',
    url = 'https://github.com/L-Chris/game-assistant',
    author = 'L-Chris',
    author_email = '563303226@qq.com',

    include_package_data = True,
    platforms = 'any',
    install_requires = ['pillow', 'pywin32', 'aircv', 'opencv3']
)