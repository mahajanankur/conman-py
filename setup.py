#!/usr/bin/env python

from setuptools import find_packages, setup

requires = [
    'python-dotenv==1.0.0'
]

setup(
    include_package_data=True,
    name="pyconman",
    version='0.0.4',
    description='Package for managing and profiling JSON configurations in Python-based libraries and web applications.',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    author='Ankur Mahajan',
    author_email='mahajanankur.nith@gmail.com',
    url='https://mahajanankur.github.io',
    packages=find_packages(exclude=['tests*']),
    install_requires=requires,
    license="Apache License",
    python_requires=">= 3",
    project_urls={
        'Documentation': 'https://github.com/mahajanankur/conman-py/blob/main/README.md',
        'Source': 'https://github.com/mahajanankur/conman-py',
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)