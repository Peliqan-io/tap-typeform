#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="tap-typeform",
    version="2.2.0",
    description="Singer.io tap for extracting data from the TypeForm Responses API",
    author="bytcode.io",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    install_requires=[
        "singer-python @ git+https://github.com/peliqan-io/singer-python@master",
        "pendulum",
        "ratelimit",
        "backoff==1.8.0",
        "requests",
        "parameterized",
    ],
    extras_require={
        'dev': [
            'pylint',
            'ipdb',
            'nose',
        ]
    },
    entry_points="""
    [console_scripts]
    tap-typeform=tap_typeform:main
    """,
    packages=find_packages(),
    package_data = {
        "schemas": ["tap_typeform/schemas/*.json"]
    },
    include_package_data=True
)
