from fastpublicsuffix import init_suffix_tree, get_root_domain


def test():
    init_suffix_tree()

    # The first set of tests here are derived from
    # http://publicsuffix.org/list/test.txt
    for domain, expected in (
        (None, None),
        ('COM', None),
        ('WwW.example.COM', 'example.com'),

        ('example.local', None),
        ('a.b.example.local', None),

        ('biz', None),
        ('domain.biz', 'domain.biz'),
        ('b.domain.biz', 'domain.biz'),
        ('a.b.domain.biz', 'domain.biz'),

        ('example.com', 'example.com'),
        ('b.example.com', 'example.com'),
        ('a.b.example.com', 'example.com'),
        ('uk.com', None),
        ('example.uk.com', 'example.uk.com'),
        ('b.example.uk.com', 'example.uk.com'),
        ('a.b.example.uk.com', 'example.uk.com'),
        ('test.ac', 'test.ac'),

        ('cy', None),
        ('c.cy', None),
        ('b.c.cy', 'b.c.cy'),
        ('a.b.c.cy', 'b.c.cy'),

        ('jp', None),
        ('test.jp', 'test.jp'),
        ('www.test.jp', 'test.jp'),
        ('ac.jp', None),
        ('test.ac.jp', 'test.ac.jp'),
        ('www.test.ac.jp', 'test.ac.jp'),
        ('kyoto.jp', None),

        # The following 3 tests are changed from those at
        # http://publicsuffix.org/list/test.txt, due to changes in the list on
        # 4th July 2012: http://hg.mozilla.org/mozilla-central/rev/290afd57d2a8
        # The 2 tests following these are added to further test this update.
        ('c.kyoto.jp', 'c.kyoto.jp'),
        ('b.c.kyoto.jp', 'c.kyoto.jp'),
        ('a.b.c.kyoto.jp', 'c.kyoto.jp'),
        ('muko.kyoto.jp', None),
        ('foo.muko.kyoto.jp', 'foo.muko.kyoto.jp'),
        ('pref.kyoto.jp', 'pref.kyoto.jp'),
        ('www.pref.kyoto.jp', 'pref.kyoto.jp'),

        ('om', None),
        ('test.om', None),
        ('b.test.om', 'b.test.om'),
        ('a.b.test.om', 'b.test.om'),
        ('songfest.om', 'songfest.om'),
        ('www.songfest.om', 'songfest.om'),

        ('us', None),
        ('test.us', 'test.us'),
        ('www.test.us', 'test.us'),
        ('ak.us', None),
        ('test.ak.us', 'test.ak.us'),
        ('www.test.ak.us', 'test.ak.us'),
        ('k12.ak.us', None),
        ('test.k12.ak.us', 'test.k12.ak.us'),
        ('www.test.k12.ak.us', 'test.k12.ak.us'),

        # End of tests derived from http://publicsuffix.org/list/test.txt

        # Test a unicode domain.
        (u'\U0001f4a9.com', u'\U0001f4a9.com'),

        # Test that a completely unknown domain is not passed
        ('randomhost', None),

        # Test handling of domains reserved by RFC2606
        ('test', None),
        ('.test', None),
        ('foo.test', None),
        ('example', None),
        ('.example', None),
        ('foo.example', None),
        ('invalid', None),
        ('.invalid', None),
        ('foo.invalid', None),
        ('localhost', None),
        ('.localhost', None),
        ('foo.localhost', None),

        # Test some uk domains.
        ('bl.uk', 'bl.uk'),
        ('www.bl.uk', 'bl.uk'),
        ('co.uk', None),
        ('foo.co.uk', 'foo.co.uk'),
        ('www.foo.co.uk', 'foo.co.uk'),
        ('gov.uk', None),
        ('www.gov.uk', 'www.gov.uk'),
    ):
        assert get_root_domain(domain) == expected
