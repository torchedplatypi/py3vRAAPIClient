import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='vra7_rest_wrapper',
      version='1.0.3',
      description='vRealize Automation API Client',
      author='torchedplatypi',
      author_email='torchedplatypi@gmail.com',
      install_requires=['requests', 'prettytable'],
      packages=['vra7_rest_wrapper'],
      long_description=read('README.md'),
      keywords=['VMWare', 'vRealize Automation', 'vRA'],
      classifiers=[
          'Environment :: No Input/Output (Daemon)',
          'Intended Audience :: Information Technology',
          'Intended Audience :: System Administrators',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Programming Language :: Python :: 2.7',
      ],
      zip_safe=True)
