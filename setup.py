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
    name='python_in_out_context_manager',
    version='0.1.0',
    description="Context manager that opens two files, one to read, and one to write",
    long_description=readme + '\n\n' + history,
    author="Perry Evans",
    author_email='samesense@gmail.com',
    url='https://github.com/samesense/python_in_out_context_manager',
    packages=[
        'python_in_out_context_manager',
    ],
    package_dir={'python_in_out_context_manager':
                 'python_in_out_context_manager'},
    entry_points={
        'console_scripts': [
            'python_in_out_context_manager=python_in_out_context_manager.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='python_in_out_context_manager',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
