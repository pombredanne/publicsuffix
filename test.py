from publicsuffix import init_suffix_tree, get_root_domain

def test(domain, expected):
    result = get_root_domain(domain)
    if result != expected:
        print 'FAILED: tree.match(%s) -> %s, should be %s' % (domain, result, expected)
        return
    print 'tree.match(%s) => %s' % (domain, result)

if __name__ == "__main__":

    init_suffix_tree('names.dat')

    # The first set of tests here are derived from
    # http://publicsuffix.org/list/test.txt
    test(None, None)
    test('COM', None)
    test('WwW.example.COM', 'example.com')

    test('example.local', None)
    test('a.b.example.local', None)

    test('biz', None)
    test('domain.biz', 'domain.biz')
    test('b.domain.biz', 'domain.biz')
    test('a.b.domain.biz', 'domain.biz')

    test('example.com', 'example.com')
    test('b.example.com', 'example.com')
    test('a.b.example.com', 'example.com')
    test('uk.com', None)
    test('example.uk.com', 'example.uk.com')
    test('b.example.uk.com', 'example.uk.com')
    test('a.b.example.uk.com', 'example.uk.com')
    test('test.ac', 'test.ac')

    test('cy', None)
    test('c.cy', None)
    test('b.c.cy', 'b.c.cy')
    test('a.b.c.cy', 'b.c.cy')

    test('jp', None)
    test('test.jp', 'test.jp')
    test('www.test.jp', 'test.jp')
    test('ac.jp', None)
    test('test.ac.jp', 'test.ac.jp')
    test('www.test.ac.jp', 'test.ac.jp')
    test('kyoto.jp', None)
    # The following 3 tests are changed from those at
    # http://publicsuffix.org/list/test.txt, due to changes in the list on 4th
    # July 2012: http://hg.mozilla.org/mozilla-central/rev/290afd57d2a8
    # The 2 tests following these are added to further test this update.
    test('c.kyoto.jp', 'c.kyoto.jp')
    test('b.c.kyoto.jp', 'c.kyoto.jp')
    test('a.b.c.kyoto.jp', 'c.kyoto.jp')
    test('muko.kyoto.jp', None)
    test('foo.muko.kyoto.jp', 'foo.muko.kyoto.jp')
    test('pref.kyoto.jp', 'pref.kyoto.jp')
    test('www.pref.kyoto.jp', 'pref.kyoto.jp')

    test('om', None)
    test('test.om', None)
    test('b.test.om', 'b.test.om')
    test('a.b.test.om', 'b.test.om')
    test('songfest.om', 'songfest.om')
    test('www.songfest.om', 'songfest.om')

    test('us', None)
    test('test.us', 'test.us')
    test('www.test.us', 'test.us')
    test('ak.us', None)
    test('test.ak.us', 'test.ak.us')
    test('www.test.ak.us', 'test.ak.us')
    test('k12.ak.us', None)
    test('test.k12.ak.us', 'test.k12.ak.us')
    test('www.test.k12.ak.us', 'test.k12.ak.us')

    # End of tests derived from http://publicsuffix.org/list/test.txt

    # Test a unicode domain.
    test(u'\U0001f4a9.com',u'\U0001f4a9.com')

    # Test that a completely unknown domain is not passed
    test('randomhost', None)

    # Test handling of domains reserved by RFC2606
    test('test', None)
    test('.test', None)
    test('foo.test', None)
    test('example', None)
    test('.example', None)
    test('foo.example', None)
    test('invalid', None)
    test('.invalid', None)
    test('foo.invalid', None)
    test('localhost', None)
    test('.localhost', None)
    test('foo.localhost', None)

    # Test some uk domains.
    test('bl.uk', 'bl.uk')
    test('www.bl.uk', 'bl.uk')
    test('co.uk', None)
    test('foo.co.uk', 'foo.co.uk')
    test('www.foo.co.uk', 'foo.co.uk')
    test('gov.uk', None)
    test('www.gov.uk', 'www.gov.uk')
