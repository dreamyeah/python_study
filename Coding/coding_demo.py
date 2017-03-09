#coding=utf-8

s = '中文'
print type(s), len(s)

u = u'中文'
print type(u), len(u)

u2s = u'中文'.encode('utf-8')
print type(u2s), len(u2s)

s = '中文'
print type(s)
u = s.decode('utf-8')
print type(u)

s2 = u.encode('utf-8')
print type(s2)