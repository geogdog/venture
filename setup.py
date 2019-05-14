# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='venture',
    use_scm_version=True,
    description='Project management CLI tool',
    long_description=readme,
    author='Greg Trahair',
    author_email='greg@mwb.io',
    url='https://github.com/geogdog/venture',
    license=license,
    packages=find_packages(exclude=['tests', 'docs']),
    entry_points={
        'console_scripts': [
            'venture = venture.cli:main'
        ]
    }
)
