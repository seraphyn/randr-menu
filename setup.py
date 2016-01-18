#!/usr/bin/env python3

from distutils.core import setup

setup(name='randr_menu',
      version='0.1',
      description='Appindicator Menu for Display Profiles Using XRandR',
      author='Michael Thompson',
      author_email='mt@trustdarkness.com',
      url='https://github.com/trustdarkness/randr-menu',
      py_modules=['randr_menu'],
      data_files=[('/usr/bin', ['randr_menu']),
                  ('/usr/bin', ['detect-displaylink'])],
      license='GPL v2.0',
)

