#!/usr/bin/env python3

from distutils.core import setup

setup(name='randr_menu',
      version='0.1',
      description='Appindicator Menu for Display Profiles Using XRandR',
      author='Michael Thompson',
      author_email='mt@trustdarkness.com',
      url='https://github.com/trustdarkness/randr-menu',
      py_modules=['randr_menu'],
      data_files=[('/usr/bin', ['randr-menu']),
                  ('/usr/bin', ['detect-displaylink']),
                  ('/usr/share/applications', ['randr-menu.desktop'])],
      license='GPL v2.0',
)

