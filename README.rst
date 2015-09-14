MoinMoin - Wiki Engine
======================

`MoinMoin`_ is an easy to use and extensible Wiki engine implemented in
Python with a large community of users. MoinMoin's storage mechanism are
flat files and folders, rather than a database. This makes it easy to
manipulate the content in a text editor on the server if necessary,
including managing revisions if the wiki gets attacked by spammers.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- MoinMoin configurations:
   
   - Installed from package management.
   - Wiki data maintained in /var/www/moin/mywiki.
   - Enabled FCKeditor by default (ease of use).
   - Use Apache WSGI (performance).
   - Added spellchecker with English dictionary.
   - Set character encoding to utf-8 (internationalization).
   - Set logo image to moinmoin logo and set default theme to
     rightsidebar (user experience).

- SSL support out of the box.
- Postfix MTA (bound to localhost) to allow sending of email
  (e.g., password recovery).
- Webmin modules for configuring Apache2 and Postfix.

- FCKeditor enabled by default. If required, it can be disabled::

    sed -i "s|editor_force = False|editor_force = True|" /etc/moin/mywiki.py
    /etc/init.d/apache2 restart

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, Webshell, SSH, MySQL: username **root**
-  MoinMoin: username **admin**


.. _MoinMoin: http://moinmo.in
.. _TurnKey Core: https://www.turnkeylinux.org/core
