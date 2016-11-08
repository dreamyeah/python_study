#coding: utf-8

def debug(func):
    def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
        print "[DEBUG]: enter {}()".format(func.__name__)
        print 'Prepare and say...',
        return func(*args, **kwargs)
    return wrapper  # 返回
 
@ debug
def say1(something):
    print "hello {}!".format(something)

def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print "[{level}]: enter function {func}()".format(
                level=level,
                func=func.__name__)
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper
 
@logging(level='INFO')
def say2(something):
    print "say {}!".format(something)
 
# 如果没有使用@语法，等同于
# say = logging(level='INFO')(say)
 
@logging(level='DEBUG')
def do(something):
    print "do {}...".format(something)

#不带参数的类装饰器
class logging(object):
    def __init__(self, func):
        self.func = func
 
    def __call__(self, *args, **kwargs):
        print "[DEBUG]: enter function {func}()".format(
            func=self.func.__name__)
        return self.func(*args, **kwargs)
@logging
def say3(something):
    print "say {}!".format(something)


#带参数的类装饰器
class logging(object):
    def __init__(self, level='INFO'):
        self.level = level
        
    def __call__(self, func): # 接受函数
        def wrapper(*args, **kwargs):
            print "[{level}]: enter function {func}()".format(
                level=self.level,
                func=func.__name__)
            func(*args, **kwargs)
        return wrapper  #返回函数
 
@logging(level='INFO')
def say4(something):
    print "say {}!".format(something)
if __name__ == '__main__':

	say1("dream yeah")
	say2("dream yeah")
	say3("dream yeah")
	say4("dream yeah")
	do("fuck")