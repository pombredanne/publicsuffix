from publicsuffix import init_suffix_tree, get_root_domain

def test(domain, expected):
    result = get_root_domain(domain)
    if result != expected:
        print 'FAILED: tree.match(%s) -> %s, should be %s' % (domain, result, expected)
        return
    print 'tree.match(%s) => %s' % (domain, result)

if __name__ == "__main__":

    init_suffix_tree('names.dat')

    #tests are from http://publicsuffix.org/list/test.txt
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
    test('c.kyoto.jp', None)
    test('b.c.kyoto.jp', 'b.c.kyoto.jp')
    test('a.b.c.kyoto.jp', 'b.c.kyoto.jp')
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

    test(u'\U0001f4a9.com',u'\U0001f4a9.com')
