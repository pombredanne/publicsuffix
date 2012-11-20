#!/usr/bin/env pytthon

import os.path
import urllib
import publicsuffix

outdir = os.path.dirname(__file__)
outpath = os.path.join(outdir, 'fastpublicsuffix/public_suffix_list.txt')
with file(outpath, 'w') as out_fd:
    in_fd = urllib.urlopen(publicsuffix.EFFECTIVE_TLD_NAMES)
    try:
        data = in_fd.read()
        out_fd.write(data)
    finally:
        in_fd.close()
print "Downloaded %d bytes, stored in %s" % (len(data), outpath)
