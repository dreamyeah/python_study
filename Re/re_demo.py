import re

def test_patterns(text, patterns=[]):
    """Given source text and a list of patterns, look for
    matches for each pattern within the text and print
    them to stdout.
    """
    # Show the character positions and input text
    print
    print ''.join(str(i / 10 or ' ') for i in range(len(text)))
    print ''.join(str(i % 10) for i in range(len(text)))
    print text

    # Look for each pattern in the text and print the results
    for pattern in patterns:
        print
        print 'Matching "%s"' % pattern
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            print '  %2d : %2d = "%s"' % \
                (s, e - 1, text[s:e])
    return

if __name__ == '__main__':
    patterns = [ 'this', 'that' ]
    text = 'Does this text match the pattern?'
    
    for pattern in patterns:
        print 'Looking for "%s" in "%s" ->' % (pattern, text),
    
        if re.search(pattern, text):
            print 'found a match!'
        else:
            print 'no match'
    print "-------------------------------"
    pattern = 'this'
    text = 'Does this text match the pattern?'
    
    match = re.search(pattern, text)
    
    s = match.start()
    e = match.end()
    
    print 'Found "%s" in "%s" from %d to %d ("%s")' % \
        (match.re.pattern, match.string, s, e, text[s:e])
        
    
    print "-------------------------------"  
    # Pre-compile the patterns
    regexes = [ re.compile(p) for p in [ 'this',
                                         'that',
                                         ]
                ]
    text = 'Does this text match the pattern?'
    
    for regex in regexes:
        print 'Looking for "%s" in "%s" ->' % (regex.pattern, text),
    
        if regex.search(text):
            print 'found a match!'
        else:
            print 'no match'
            
            
    print "-------------------------------"  
    text = 'abbaaabbbbaaaaa'

    pattern = 'ab'
    
    for match in re.findall(pattern, text):
        print 'Found "%s"' % match



    print "-------------------------------"          
    text = 'abbaaabbbbaaaaa'

    pattern = 'ab'
    
    for match in re.finditer(pattern, text):
        s = match.start()
        e = match.end()
        print 'Found "%s" at %d:%d' % (text[s:e], s, e)
        
    print "-------------------------------"  
    test_patterns('abbaaabbbbaaaaa', ['ab'])
    
    print "-------greedy------------------------"    
    test_patterns('abbaaabbbbaaaaa',
              [ 'ab*',  # a followed by zero or more b
                'ab+',  # a followed by one or more b
                'ab?',  # a followed by zero or one b
                'ab{3}',  # a followed by three b
                'ab{2,3}',  # a followed by two to three b
                ])
    
    print "--------ungreedy-----------------------"
    test_patterns('abbaaabbbbaaaaa',
              [ 'ab*?',  # a followed by zero or more b
                'ab+?',  # a followed by one or more b
                'ab??',  # a followed by zero or one b
                'ab{3}?',  # a followed by three b
                'ab{2,3}?',  # a followed by two to three b
                ])
    
    print "--------Character Sets 1-----------------------"
    test_patterns('abbaaabbbbaaaaa',
              [ '[ab]',  # either a or b
                'a[ab]+',  # a followed by one or more a or b
                'a[ab]+?',  # a followed by one or more a or b, not greedy
                ])
    print "--------Character Sets 2-----------------------"
    test_patterns('This is some text -- with punctuation.',
              [ '[^-. ]+',  # sequences without -, ., or space
                ])
    
    print "--------Character Sets 3-----------------------"
    test_patterns('This is some text -- with punctuation.',
              [ '[a-z]+',  # sequences of lower case letters
                '[A-Z]+',  # sequences of upper case letters
                '[a-zA-Z]+',  # sequences of lower or upper case letters
                '[A-Z][a-z]+',  # one upper case letter followed by lower case letters
                ])
    
    print "--------Character Sets 4-----------------------"
    test_patterns('abbaaabbbbaaaaa',
              [ 'a.',  # a followed by any one character
                'b.',  # b followed by any one character
                'a.*b',  # a followed by anything, ending in b
                'a.*?b',  # a followed by anything, ending in b
                ])
    print "--------Character Sets 5-----------------------"
    test_patterns('This is a prime #1 example!',
              [ r'\d+',  # sequence of digits
                r'\D+',  # sequence of non-digits
                r'\s+',  # sequence of whitespace
                r'\S+',  # sequence of non-whitespace
                r'\w+',  # alphanumeric characters
                r'\W+',  # non-alphanumeric
                ])
    
    
    print "--------Character Sets 6-----------------------"
    test_patterns(r'\d+ \D+ \s+ \S+ \w+ \W+',
              [ r'\\d\+',
                r'\\D\+',
                r'\\s\+',
                r'\\S\+',
                r'\\w\+',
                r'\\W\+',
                ])
    
    
    print "--------Character Sets 7-----------------------"
    test_patterns('This is some text -- with punctuation.',
              [ r'^\w+',  # word at start of string
                r'\A\w+',  # word at start of string
                r'\w+\S*$',  # word at end of string, with optional punctuation
                r'\w+\S*\Z',  # word at end of string, with optional punctuation
                r'\w*t\w*',  # word containing 't'
                r'\bt\w+',  # 't' at start of word
                r'\w+t\b',  # 't' at end of word
                r'\Bt\B',  # 't', not start or end of word
                ])
    
    
    print "--------Character Sets 8-----------------------"
    print '''In situations where you know in advance that only a subset of the full input should be searched, you can further constrain the regular expression match by telling re to limit the search range. For example, if your pattern must appear at the front of the input, then using match() instead of search() will anchor the search without having to explicitly include an anchor in the search pattern.'''

    text = 'This is some text -- with punctuation.'
    pattern = 'is'
    
    print 'Text   :', text
    print 'Pattern:', pattern
    
    m = re.match(pattern, text)
    print 'Match  :', m
    s = re.search(pattern, text)
    print 'Search :', s
    
    
    print "--------Character Sets 9-----------------------"
    test_patterns('abbaaabbbbaaaaa',
              [ 'a(ab)',    # 'a' followed by literal 'ab'
                'a(a*b*)',  # 'a' followed by 0-n 'a' and 0-n 'b'
                'a(ab)*',   # 'a' followed by 0-n 'ab'
                'a(ab)+',   # 'a' followed by 1-n 'ab'
                ])
