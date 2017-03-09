#coding=utf-8

class people:
    name = 'jack'  #公有的类属性
    __age = 12     #私有的类属性

p = people()

print p.name             #正确
print people.name        #正确
# print p.__age            #错误，不能在类外通过实例对象访问私有的类属性
# print people.__age       #错误，不能在类外通过类对象访问私有的类属性


class people:
    name = 'jack'
    
    #__init__()是内置的构造方法，在实例化对象时自动调用
    def __init__(self,age):
        self.age = age

p = people(12)
print p.name    #正确
print p.age     #正确

print people.name    #正确
# print people.age     #错误

class people:
    name = 'jack'
    
    #__init__()是内置的构造方法，在实例化对象时自动调用
    def __init__(self,age):
        self.age = age

p = people(12)
print p.name    #正确
print p.age     #正确

print people.name    #正确
# print people.age     #错误

class people:
    country = 'china'
    

print people.country
p = people()
print p.country
p.country = 'japan' 
print p.country      #实例属性会屏蔽掉同名的类属性
print people.country
del p.country    #删除实例属性
print p.country

class people:
    country = 'china'
    
    #类方法，用classmethod来进行修饰
    @classmethod
    def getCountry(cls):
        return cls.country

p = people()
print p.getCountry()    #可以用过实例对象引用
print people.getCountry()    #可以通过类对象引用

class people:
    country = 'china'
    
    #类方法，用classmethod来进行修饰
    @classmethod
    def getCountry(cls):
        return cls.country
        
    @classmethod
    def setCountry(cls,country):
        cls.country = country
        

p = people()
print p.getCountry()    #可以用过实例对象引用
print people.getCountry()    #可以通过类对象引用

p.setCountry('japan')   

print p.getCountry()   
print people.getCountry()


class people:
    country = 'china'
    
    #实例方法
    def getCountry(self):
        return self.country
        

p = people()
print p.getCountry()         #正确，可以用过实例对象引用
# print people.getCountry()    #错误，不能通过类对象引用实例方法

class people:
    country = 'china'
    
    @staticmethod
    #静态方法
    def getCountry():
        return people.country
        
print '-----------'
print people.getCountry()
p = people()
print '-----------'
p.getCountry()

# 从类方法和实例方法以及静态方法的定义形式就可以看出来，类方法的第一个参数是类对象cls，那么通过cls引用的必定是类对象的属性和方法；而实例方法的第一个参数是实例对象self，那么通过self引用的可能是类属性、也有可能是实例属性（这个需要具体分析），不过在存在相同名称的类属性和实例属性的情况下，实例属性优先级更高。静态方法中不需要额外定义参数，因此在静态方法中引用类属性的话，必须通过类对象来引用。