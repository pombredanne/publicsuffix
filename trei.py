
EFFECTIVE_TLD_NAMES = 'http://mxr.mozilla.org/mozilla-central/source/netwerk/dns/effective_tld_names.dat?raw=1'

def _normalize(s):
    if s.startswith('.'):
        s = s[1:]
    #rules end at the first white space
    s = s.split()[0]
    s = s.lower()
    s = s.decode('utf-8')
    return s

class PrefixNode:
    '''
    An internal class, each prefix in the tree represents a part of a domain name. (e.g. '.com')
    The naming is a little confusing, a PrefixTree is the data structure, but the nodes are
    used to store the suffixes of partial domain names.
    '''

    #passing a rule lets you build on entire branch in one call
    def __init__(self, prefix, rule=None):
        if prefix is not None:
            self.is_exception = prefix.startswith('!')
            if self.is_exception:
                prefix = prefix[1:]
        self.prefix = prefix
        self.children = dict()
        if rule is not None:
            self.add(rule)

    def __repr__(self):
        return 'PrefixNode(\'%s\')' % (self.prefix,)

    def add(self, rule):
        if len(rule) == 0:
            return
        prefix = rule[0]
        if prefix.startswith('!') and '*' in self.children:
            #if this is an exception to a wildcard it should be a child of that wildcard
            self.children['*'].add(rule)
            return
        if prefix in self.children:
            self.children[prefix].add(rule[1:])
        else:
           if prefix.startswith('!'):
               prefix = prefix[1:]
           self.children[prefix] = PrefixNode( prefix, rule= rule[1:] )

    # when given a rule to match, splits the tuple into a matching section and the domain name
    # e.g. match( ('com', 'example', 'www') ) -> ( ['.com'], 'example' )
    # e.g. match( ('com', 'eff-tld', 'site') ) -> ( ['.eff-tld', '.com'], 'site' )
    def match(self, rule):
        #print ' %s is matching %s' % (self.prefix, rule)
        if len(rule) == 0:
            #when a tld is also a hostname
            return ( [], [])
        if self.prefix == '*':
            return self._match_as_wildcard(rule)
        prefix = rule[0]
        if prefix not in self.children:
            if '*' in self.children:
                return self.children['*'].match(rule)
            return ( [], prefix )
        else:
            match = self.children[prefix].match( rule[1:] )
            child_matched = match[0]
            child_matched.append('.' + prefix)
            return ( child_matched, match[1] ) 

    def _match_as_wildcard(self, rule):
        #print '  %s: matching %s as wildcard. My children are: %s' % (self.prefix, rule, self.children)
        prefix = rule[0]
        #if prefix matches no exception
        if prefix not in self.children:
            if len(rule) > 1:
                return ( ['.' + prefix], rule[1])
            return ( ['.' + prefix], None)
        else:
            return ( [], prefix)

class PrefixTree(PrefixNode):
    '''
    Helper to provide a nicer interface for dealing with the tree
    '''
    #seq is a sequence of tuples representing rules
    #of the form ('com'), ('uk', 'co'), etc.
    def __init__(self, seq):
        PrefixNode.__init__(self, None)
        for rule in seq:
            self.add(rule)	

    def __repr__(self):
        return '<PrefixTree (%s children)>' % (len(self.children),)

    def match(self, s):
        rule = tuple(reversed(s.strip().split('.')))
        match = PrefixNode.match(self, rule)
        #print 'Tree matching %s, match was %s' % (s, match)
        if len(match[0]) == 0:
            return None
        return (''.join(match[0]), match[1])

    def domain(self, s):
        if s is None:
            return None
        s = _normalize(s)
        match = self.match(s)
        try:
            return match[1] + match[0]
        except:
            return None

def _tokenize(lines):
    rules = []
    for s in lines:
        if s and not s.isspace() and not s.startswith('//'):
            rule = tuple(reversed(_normalize(s).split('.')))
            rules.append(rule)

    return rules

def load(filename):
    names = open(filename, 'r')
    lines = names.readlines()
    names.close()
    tuples = _tokenize(lines)
    return PrefixTree(tuples)

def test(domain, expected):
    result = tree.domain(domain)
    if result != expected:
        print 'FAILED: tree.match(%s) -> %s, should be %s' % (domain, result, expected)
        return
    print 'tree.match(%s) => %s' % (domain, result)

if __name__ == "__main__":

    tree = load('names.dat')

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

