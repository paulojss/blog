#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os

DEBUG = True

AUTHOR = u'Klaus Peter Laube'
SITENAME = u'Klaus Laube'
SITESUBTITLE = u'Python, Django e desenvolvimento Web'
SITEURL = os.environ.get('SITEURL', 'http://local.klauslaube.com.br:8000')
SITEDESCRIPTION = u'Artigos sobre desenvolvimento Web, Python Django, padrões Web e Linux.'
RELATIVE_URLS = False

TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = u'pt_BR'
DEFAULT_DATE_FORMAT = '%d %b, %Y'

DELETE_OUTPUT_DIRECTORY = True
WEBASSETS = True
STATIC_PATHS = ['images']
THEME = 'maggner-pelican'

PLUGIN_PATH = 'plugins'
PLUGINS = ['global_license', 'image_tag', 'summary', 'slideshare',
    'related_posts', ]

FEED_ALL_ATOM = False
FEED_ALL_RSS = 'feed/rss.xml'
TAG_FEED_RSS = 'feeds/tags/%s.xml'
USE_FOLDER_AS_CATEGORY = False
DEFAULT_PAGINATION = 10


# Article
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
TAG_URL = '/tag/{slug}.html'
TAG_CLOUD_MAX_ITEMS = 30
DISQUS_SITENAME = 'klauslaube'

# Menu
MENUITEMS = (
    ('Blog', '/'),
)

# Blogroll
LINKS = ()

# Social
SOCIAL = (
    ('Bitbucket', 'http://bitbucket.org/kplaube/'),
    ('Coderwall', 'http://coderwall.com/kplaube'),
    ('Duolingo', 'http://duolingo.com/#/kplaube'),
    ('GitHub', 'http://github.com/kplaube'),
    ('LinkedIn', 'http://www.linkedin.com/in/klauslaube'),
    ('ProfissionaisTI', 'http://www.profissionaisti.com.br/author/klaus-peter-laube/'),
    ('Skoob', 'http://skoob.com.br/usuario/118855'),
    ('Twitter', 'http://www.twitter.com/kplaube'),
    ('Zootool', 'http://zootool.com/user/kplaube/'),
)

TWITTER_USERNAME = 'kplaube'
#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""

# License
LICENSE = 'Creative Commons Attribution 3.0'
LICENSE_URL = 'http://creativecommons.org/licenses/by/3.0/deed.pt_BR'
LICENSE_TITLE = 'Share, adapt, use. But mention the author'
SOURCE_CODE_URL = 'https://github.com/kplaube/klauslaube.com.br/'
SOURCE_CODE_REPOSITORY = 'GitHub'
