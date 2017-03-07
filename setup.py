#!/usr/bin/env python

import os

from setuptools import setup


PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))


setup(
    name='djdt-sites',
    version='0.1.0',
    description='A Django Debug Toolbar panel to switch between sites',
    long_description=open(os.path.join(PROJECT_PATH, 'README.rst')).read(),
    author='Nicolas Appriou',
    author_email='nicolas.appriou@gmail.com',
    url='https://github.com/Nicals/djdt-sites',
    license='MIT',
    packages=['djdt_sites'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
