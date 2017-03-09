#coding=utf8

l = range(10)
print "l:",l
print "l[1:5]:",l[1:5]
print "l[-1]:",l[-1]
print "l[1:-1]:",l[1:-1]
print "l[1:10]:",l[1:10]
print "l[2:-2]:",l[2:-2]
print "l[1:]:",l[1:]
print "l[:]:",l[:]
#第一个：指整个list,后面的:2指步长
print "l[::2]:",l[::2]
print "l[1::2]:",l[1::2]
print "l[1:9:-1]:",l[1:9:-1]
print "l[9:1:-1]",l[9:1:-1]
print "l[9:1:-2]",l[9:1:-2]

# list[start:end:step]