#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

PACKAGE_NAME = 'robotframework-gnmi'

CLASSIFIERS = """
"""

setup(
    name=PACKAGE_NAME,
    version='0.1',
    description='RobotFramework keywords for GNMI client',
    long_description='',
    url='https://wwwin-github.cisco.com/xxxx',
    author='Oliver Boehmer',
    author_email='oboehmer@cisco.com',
    license='',
    # package_dir={'': 'src'},
    # package_data={},
    packages=['GNMI'],
    # keywords='lazymaestro genie ',
    python_requires='>=3.6',
    scripts=[],
    install_requires=['robotframework>=3.0', 'pygnmi>=0.6.8'],
    dependency_links=[],
    include_package_data=True,
    zip_safe=False,
)
