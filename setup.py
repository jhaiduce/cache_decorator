"""Config for PyPI."""

from setuptools import find_packages
from setuptools import setup

requires=['backports.functools_lru_cache']

setup(
    author='John Haiducek',
    author_email='jhaiduce@umich.edu',
    version='0.0.1',
    zip_safe=True,
    packages=['cache_decorator'],
    name='cache_decorator',
    install_requires=requires
)
