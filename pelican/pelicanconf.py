#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
from os.path import join as pjoin

_CUR_DIR = os.path.dirname(os.path.abspath(__file__))
_THEME_PATH = pjoin(_CUR_DIR, 'theme-mockingbird')
_OUTPUT_PATH = pjoin(_CUR_DIR, 'output')
_POSTS_PATH = pjoin(os.path.dirname(_CUR_DIR), 'posts')

AUTHOR = u'Mahmoud Hashemi'
SITENAME = u'Sedimental'
SITEURL = ''
TIMEZONE = "America/Los_Angeles"

THEME = _THEME_PATH
OUTPUT_PATH = _OUTPUT_PATH
PATH = _POSTS_PATH

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Github', 'https://github.com/mahmoud'),
         ('Wikipedia', 'http://en.wikipedia.org/wiki/User:MahmoudHashemi'))

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
