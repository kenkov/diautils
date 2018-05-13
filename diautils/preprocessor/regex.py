#! /usr/bin/env python
# coding:utf-8


import re


username = r'[a-zA-Z0-9_]+'
url = re.compile(r'(http|https)://[a-zA-Z0-9-./"#$%&\':?=_]+')
mention = re.compile(r'@{}'.format(username))
head_mention = re.compile(r'^@{}'.format(username))
retweet = re.compile(r'(RT|QT) {}:'.format(username))
tag = re.compile(r'#[a-zA-Z0-9_]+')