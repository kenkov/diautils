#! /usr/bin/env python
# coding:utf-8

from distutils.core import setup


setup(
    name="diautils",
    packages=["diautils", "diautils.preprocessor"],
    install_requires=[
        "emoji==0.5.0",
        "fire==0.1.3",
        "mojimoji==0.0.8",
        ],
    version="0.1.1",
    author="kenkov",
    author_email="kenkovtan@gmail.com",
    url="http://kenkov.jp",
)
