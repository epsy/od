#!/usr/bin/env python

from setuptools import setup

setup(
    name='od',
    version='1.0',
    description='Shorthand syntax for building OrderedDicts',
    license='MIT',
    url='https://github.com/epsy/od',
    author='Yann Kaiser',
    author_email='kaiser.yann@gmail.com',
    py_modules=('od', 'test_od'),
    tests_require=['unittest2', 'repeated_test'],
    test_suite='unittest2.collector',
    keywords=[
        'OrderedDict', 'od', 'syntactic sugar',
        ],
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        ],
)
