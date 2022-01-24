#!/usr/bin/env python

import pathlib
from setuptools import setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.rst").read_text(encoding='utf-8')


setup(
    name='od',
    version='2.0.1',
    description='Shorthand syntax for building OrderedDicts',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    license='MIT',
    url='https://github.com/epsy/od',
    author='Yann Kaiser',
    author_email='kaiser.yann@gmail.com',
    py_modules=('od', 'test_od'),
    extras_require={
        'test': ['repeated_test'],
    },
    keywords=[
        'OrderedDict', 'od', 'syntactic sugar',
        ],
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        ],
)
