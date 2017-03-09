A.正则表达式，使用IGNORECASE标志
>>> import re
>>> m = re.search('multi', 'A mUltiCased string', re.IGNORECASE)
>>> bool(m)
True
B.在比较前把2个字符串转换成同样大写，用upper()方法，或小写,lower()
>>> s = 'A mUltiCased string'.lower()
>>> s
'a multicased string'
>>> s.find('multi')
2
reference: