# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='dotlinker',
    version='0.1.2',
    description='Links dotfiles',
    long_description=readme,
    author='Dotan Nahum',
    data_files=[('', ['LICENSE', 'README.md'])],
    author_email='jondotan@gmail.com',
    url='https://github.com/jondot/dotlinker',
    license=license,
    py_modules=['dotlinker'],
    entry_points='''
        [console_scripts]
        dotlinker=dotlinker:main
    ''',
    # packages=find_packages(exclude=('tests', 'docs', 'jest-pytest')),
    install_requires=['toolz', 'docopt'])
