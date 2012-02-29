====================
txWS Example Project
====================

:Author: Gregory Taylor
:Based on: zed's gist_

This repository serves as a quick foundation to build WebSockets-driven
projects using txWS_. A basic structure has been provided for you to build on.

.. _txWS: https://github.com/MostAwesomeDude/txWS
.. _gist: https://gist.github.com/1380305

Installing
==========

To install the example project, you should only need a recent version of
Twisted_, and txWS_. If you have pip::

    pip install --upgrade twisted txws

Or easy_install::

    easy_install -U twisted txws

.. _Twisted: http://twistedmatrix.com/

Running
=======

Simply ``cd`` to the ``txws-example-project`` directory and::

    twistd -ny server.tac

You can then open up any of the HTML files under the ``static`` sub-directory
to see a few examples. While it's easiest to open the files locally while
testing, these may also be served using your choice of webserver
(Apache, NGINX).

To run the unit tests, make sure you're still in the project's root directory
and::

    PYTHONPATH=. python tests/test_streamer.py

License
=======

This project is licensed under the WTFPL_.

.. _WTFPL: http://sam.zoy.org/wtfpl/