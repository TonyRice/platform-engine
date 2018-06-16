#!/usr/bin/env python
import io
import os
import sys

from setuptools import find_packages, setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()


readme = io.open('README.rst', 'r', encoding='utf-8').read()

setup(
    name='asyncy-platform-engine',
    description='The engine of the Asyncy platform',
    long_description=readme,
    author='Asyncy',
    author_email='noreply@asyncy.com',
    version='0.0.2',
    packages=find_packages(),
    tests_require=[
        'pytest',
        'pytest-cov',
        'pytest-mock',
        'pytest-asyncio'
    ],
    setup_requires=['pytest-runner'],
    install_requires=[
        'prometheus-client==0.2.0',
        'tornado==5.0.2',
        'click>=6.7',
        'cryptography>=2.1.4',
        'dateparser>=0.7.0',
        'frustum>=0.0.1',
        'raven==6.8.0',
        'storyscript>=0.0.7',
        'ujson>=1.35'
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ],
    entry_points="""
        [console_scripts]
        asyncy-server=asyncy.Service:Service.main
    """
)
