try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '0.0.1'

setup(
    name='py-multicodec',
    version=version,
    description='Self-describing serialization. This is a python implementation of https://github.com/jbenet/multicodec',
    author='Fred Thomsen',
    license='Apache License'
)
