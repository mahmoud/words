# -*- coding: utf-8 -*-
from __future__ import unicode_literals

AUTHOR = 'Mahmoud Hashemi'
SITENAME = 'Sedimental'
SITEURL = 'http://mahmoud.github.io/words'
TIMEZONE = "America/Los_Angeles"

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

THEME = 'pelican-mockingbird'
OUTPUT_PATH = 'output'
PATH = 'posts'

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'

DIRECT_TEMPLATES = ['index', 'blog', 'tags', 'categories', 'archives']
PAGINATED_DIRECT_TEMPLATES = ['blog', 'archives']


GITHUB_URL = 'http://github.com/mahmoud/words'
DISQUS_SITENAME = ''
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_PAGINATION = 4
DEFAULT_DATE = (2014, 1, 1, 1, 1, 1)

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

LINKS = (('Github', 'https://github.com/mahmoud'),
         ('Wikipedia', 'http://en.wikipedia.org/wiki/User:MahmoudHashemi'))

# global metadata to all the contents
DEFAULT_METADATA = []

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'}}

# static paths will be copied without parsing their contents
STATIC_PATHS = ['extra/robots.txt']

# custom page generated with a jinja2 template
TEMPLATE_PAGES = {'pages/jinja2_template.html': 'jinja2_template.html'}

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}
