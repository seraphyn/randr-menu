#!/usr/bin/env python3
from setuptools.command.install import install
from distutils import log
from distutils.core import setup
import os
import sys
import stat

if sys.version_info[0] < 3:
    print("Must be using Python 3")
    sys.exit(0)

class OverrideInstall(install):
  def run(self):
    uid, gid = 0, 0
    mode = 'o+rw'
    execute = stat.S_IXOTH
    read = stat.S_IROTH
    install.run(self) # calling install.run(self) insures that everything that happened previously still happens, so the installation does not break!
    # here we start with doing our overriding and private magic ..
    for filepath in self.get_outputs():
      if self.install_scripts in filepath:
        log.info("Overriding setuptools mode of scripts ...")
        log.info("Changing ownership of %s to uid:%s gid %s" %
                 (filepath, uid, gid))
        os.chown(filepath, uid, gid)
        log.info("Changing permissions of %s to %s" %
                 (filepath, mode))
        st = os.stat(filepath)
        os.chmod(filepath, st.st_mode | execute | read)


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
      cmdclass={'install': OverrideInstall}
)


