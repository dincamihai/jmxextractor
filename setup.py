# -*- coding: utf-8 -*-
from setuptools import setup
import sys
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(name='jmxextractor',
      version='0.1',
      description='Extract data from a JMeter(.jmx) file',
      url='https://github.com/dincamihai/jmxextractor.git',
      author='Mihai Dincă',
      author_email='dincamihai@gmail.com',
      license='GNU GPL v2.0',
      packages=['jmxextractor'],
      install_requires=[
        'lxml==3.4.4'
      ],
      tests_require=[
        'pytest==2.8.1',
        'pytest-pythonpath==0.7'
      ],
      cmdclass = {'test': PyTest},
      zip_safe=False)
