#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='basil',
    version='0.1.0',
    description="basil is a tool for tracking and visualizing personal finance.",
    long_description=readme + '\n\n' + history,
    author="Melissa Ko and Jordan Moldow",
    author_email='melissa.e.ko@gmail.com',
    url='https://github.com/mesako/basil',
    packages=[
        'basil',
    ],
    package_dir={'basil':
                 'basil'},
    entry_points={
        'console_scripts': [
            'basil=basil.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU Affero General Public License v3 or later (AGPLv3+)",
    zip_safe=False,
    keywords='basil',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
