#coding=utf-8

a = [1,2,3,4,5,6,7,8,9,10]
squares = map(lambda x : x**2, a)
print squares

squares1 = [x ** 2 for x in a ]
print squares1

squares2 = [x ** 2 for x in a if x % 2 == 0]
print squares2