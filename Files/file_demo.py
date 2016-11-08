#coding: utf-8
import time
with open("..//Example//file1.txt") as fp:
	for line in fp:
		print line

print '--------------------------'

with open("..//Example//file1.txt") as f:
	for line in f.readlines():
		print line

print '--------------------------'
#for big file
with open("../Example//file1.txt") as f:
	for line in f.xreadlines():
		print line

print '--------------------------'
file = open("..//Example//file2.txt","a")
file.write(time.strftime('%Y-%m-%d %X',time.localtime())+"\n")
file.close

with open("..//Example//file2.txt") as fp:
	for line in fp:
		print line


print '--------------------------'
with open("..//Example//file3.txt","w") as ff:
	ff.write(time.strftime('%Y-%m-%d %X',time.localtime())+"\n")

with open("..//Example//file3.txt") as ff:
	for line in ff:
		print line