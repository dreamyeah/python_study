#coding=utf-8
import glob
for file in glob.glob("..//Example//file[0-9].txt"):
	print file
print '-----------------'
for file in glob.glob("..//Example//file1.*"):
	print file