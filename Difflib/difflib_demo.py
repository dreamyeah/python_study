import difflib
from difflib_data import *

if __name__ == '__main__':
    d = difflib.Differ()
    diff = d.compare(text1_lines, text2_lines)
    print '\n'.join(diff)
    
    print "-------------------"
    
    diff = difflib.ndiff(text1_lines, text2_lines)
    print '\n'.join(list(diff))
    
    print "-------------------"
        
    diff = difflib.unified_diff(text1_lines, text2_lines, lineterm='')
    print '\n'.join(list(diff))
    
    print "-------------------"
     
    d = difflib.HtmlDiff()
    print d.make_table(text1_lines, text2_lines)