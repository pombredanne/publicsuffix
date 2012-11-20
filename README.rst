================
fastpublicsuffix
================

This module provides a Python interface to the `Public Suffix List`_.

The Public Suffix List (PSL) is a set of rules describing "effective top-level
domains" and can be used to determine the registered domain for a given host
name.

This module is maintained by Richard Boulton, based on a fork of a module from
`MixRank`.

Usage
-----

You can download the `list` yourself, or use the version distributed along with
the module.

Call the ``init_suffix_tree`` function. Then call
`get_root_domain` to find the registered domain. This branch does not support asking
for the (E)TLD.

Find the registered domain::

    >>> fastpublicsuffix.init_suffix_tree()
    >>> fastpublicsuffix.domain('www.python.org')
    u'python.org'

.. _`Public Suffix List`: http://publicsuffix.org/
.. _`list`: http://mxr.mozilla.org/mozilla-central/source/netwerk/dns/effective_tld_names.dat?raw=1
.. _`MixRank`: http://mixrank.com
