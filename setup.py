from distutils.core import setup

DISTNAME='git_subtree'
FULLVERSION='0.1'

setup(name=DISTNAME,
      version=FULLVERSION,
      scripts=['bin/st'], 
      packages=['git_subtree']
      )
