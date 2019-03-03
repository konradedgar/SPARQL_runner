#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Konrad <konrad.zdeb@me.com>
#
# Distributed under terms of the GPL 3-0 license.

"""
Setup script for SPARQL query runner.
"""

###########
# Modules #
###########
from distutils.core import setup


#########
# Setup #
#########

setup(name='SPARQL runner',
      version='0.1',
      author='Konrad Zdeb',
      author_email='konrad.zdeb@me.com',
      url='https://github.com/konradedgar/SPARQL_runner',
      py_modules=['sparql_runner'],
      )
