============
fastpublicsuffix
============

This module provides a Python interface to the `Public Suffix List`_.

The Public Suffix List (PSL) is a set of rules describing
"effective top-level domains" and can be used to determine the registered
domain for a given host name.

This branch is maintained by `MixRank`_, we reimplemented it using a different data structure (a prefix tree)
in order to improve performance.

Usage
-----

You will need to download the `list`_ yourself.

Call the ``init_suffix_tree`` function with the location of the list. Then call
`get_root_domain` to find the registered domain. This branch does not support asking
for the (E)TLD.

Find the registered domain::

    >>> publicsuffix.init_suffix_tree('names.dat')
    >>> publicsuffix.domain('www.python.org')
    u'python.org'

.. _`Public Suffix List`: http://publicsuffix.org/
.. _`list`: http://mxr.mozilla.org/mozilla-central/source/netwerk/dns/effective_tld_names.dat?raw=1
.. _`MixRank`: http://mixrank.com