#coding: utf-8
import time

with open("..//Example//file3.txt","w") as ff:
	ff.write(time.strftime('%Y-%m-%d %X',time.localtime())+"\n")

with open("..//Example//file3.txt") as ff:
	for line in ff:
		print line