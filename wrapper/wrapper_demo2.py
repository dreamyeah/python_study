#coding=utf-8

import time

class TimeRecorder:
	def __init__(self, name):

		self.name = name
		self.startTime = time.time()
		print name.__name__
	def __del__(self):
		print u"{0}结束，耗时：{1}".format(self.name.__name__, time.time() - self.startTime)


def time_spend1(func):
	def wrapper(*args, **kwargs):
		t = TimeRecorder(func)
		return func(*args, **kwargs)
	return wrapper

def time_spend(func):
	def wrapper(*args, **kwargs):
		print "Call %s" % func.__name__
		start = time.time()
		r = func(*args, **kwargs)
		end = time.time()
		print "Spend {0}".format(end-start)
		return r
	return wrapper

@time_spend
def test():
	time.sleep(5)

@time_spend1
def test1():
	time.sleep(5)

if __name__ == '__main__':
	test()
	test1()