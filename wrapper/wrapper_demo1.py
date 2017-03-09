#coding=utf-8
import datetime
from functools import wraps
def log(text):
	def decorator(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			print "%s : %s()" % (text, func.__name__)
			return func(*args, **kwargs)
		return wrapper
	return decorator

def log1(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		print 'call %s()' % func.__name__
		return func(*args, **kwargs)
	return wrapper

#函数执行前后打印信息
def before_end_print(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		print "Before time: %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		func(*args, **kwargs)
		print "End time: %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	return wrapper



@before_end_print
def hello(text):
	print 'say: '+text


@log1
def noww():
	print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
@log('excute')
def now():
	print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == '__main__':

	now()
	print '--------------'
	noww()
	print '--------------'
	hello('hello')

	