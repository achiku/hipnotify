#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import ast


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


_version_re = re.compile(r'__version__\s+=\s+(.*)')


with open('hipnotify/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements/common.txt') as f:
    requirements = [r.strip() for r in f.readlines()]

with open('./requirements/development.txt') as f:
    test_requirements = [r.strip() for r in f.readlines()]

setup(
    name='hipnotify',
    version=version,
    description="Deadly simple HipChat API V2 room notification library",
    long_description=readme,
    author="Akira Chiku",
    author_email='akira.chiku@gmail.com',
    url='https://github.com/achiku/hipnotify',
    packages=[
        'hipnotify',
    ],
    package_dir={'hipnotify': 'hipnotify'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='hipnotify',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
