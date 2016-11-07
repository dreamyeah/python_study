import string



if __name__ == '__main__':
    for n in dir(string):
        if n.startswith('_'):
            continue
        v = getattr(string, n)
        if isinstance(v, basestring):
            print '%s=%s' % (n, repr(v))
            print
    
    print "----------------------------"    
    s = 'The quick brown fox jumped over the lazy dog.'
    print s
    print string.capwords(s)
    
    
    print "----------------------------"
    leet = string.maketrans('abegiloprstz', '463611092572')
    s = 'The quick brown fox jumped over the lazy dog.'
    print s
    print s.translate(leet)
    
    print "----------------------------"
    values = { 'var':'foo' }
    t = string.Template("""
    $var
    $$
    ${var}iable
    """)   
    print 'TEMPLATE:', t.substitute(values)   
    s = """
    %(var)s
    %%
    %(var)siable
    """    
    print 'INTERPLOATION:', s % values
    
    print "----------------------------"
    values = { 'var':'foo' }

    t = string.Template("$var is here but $missing is not provided")
    
    try:
        print 'TEMPLATE:', t.substitute(values)
    except KeyError, err:
        print 'ERROR:', str(err)
        
    print 'TEMPLATE:', t.safe_substitute(values)
    
    
    print "----------------------------"