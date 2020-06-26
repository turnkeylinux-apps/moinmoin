#!/usr/bin/python2
"""Set MoinMoin admin password and email

Option:
    --pass=     unless provided, will ask interactively
    --email=    unless provided, will ask interactively

"""

import sys

password = sys.argv[1]
email = sys.argv[2]

from MoinMoin.web.contexts import ScriptContext
from MoinMoin import user

sys.path.append("/etc/moin")
request = ScriptContext()
cfg = request.cfg

userid = user.getUserId(request, 'admin')
u = user.User(request, userid)
u.email = email
u.enc_password = user.encodePassword(cfg, password)
u.save()
