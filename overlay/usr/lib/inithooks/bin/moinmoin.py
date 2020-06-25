#!/usr/bin/python3
"""Set MoinMoin admin password and email

Option:
    --pass=     unless provided, will ask interactively
    --email=    unless provided, will ask interactively

"""

import sys
import getopt
import inithooks_cache

from dialog_wrapper import Dialog
import subprocess

def usage(s=None):
    if s:
        print("Error:", s, file=sys.stderr)
    print("Syntax: %s [options]" % sys.argv[0], file=sys.stderr)
    print(__doc__, file=sys.stderr)
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'email='])
    except getopt.GetoptError as e:
        usage(e)

    password = ""
    email = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--email':
            email = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "MoinMoin Password",
            "Enter new password for the MoinMoin 'admin' account.")

    if not email:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        email = d.get_email(
            "MoinMoin Email",
            "Enter email address for the MoinMoin 'admin' account.",
            "admin@example.com")

    inithooks_cache.write('APP_EMAIL', email)

    # the stderr=DEVNULL is to suppress some warnings, however when debugging it
    # may be preferable to remove this.
    subprocess.run(
            ['python2', '/usr/lib/inithooks/bin/moinmoin_util.py', password, email],
            check=True, stderr=subprocess.DEVNULL)

if __name__ == "__main__":
    main()

