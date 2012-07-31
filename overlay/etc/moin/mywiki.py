# -*- coding: utf-8 -*-

from farmconfig import FarmConfig

class Config(FarmConfig):
    sitename = u'MoinMoin'
    interwikiname = 'Moin'
    show_interwiki = False
    logo_string = u'<img src="/moin_static192/common/moinmoin.png" alt="MoinMoin Logo">'

    page_front_page = u"FrontPage"

    data_dir = '/var/www/moin/mywiki/data/'
    data_underlay_dir = '/var/www/moin/mywiki/underlay/'
    cache_dir = '/var/lib/moin/cache'

    superuser = ['admin']
    theme_default = 'rightsidebar'

    mail_from = u"MoinMoin notifier <admin@example.com>"
    mail_smarthost = "127.0.0.1"

    editor_force = False
    editor_default = 'gui'
    editor_ui = 'freechoice'
