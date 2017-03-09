#coding=utf-8
class UniversityMember:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

class Student(UniversityMember):

    def __init__(self,name,age,sno,mark):
        UniversityMember.__init__(self,name,age)     #注意要显示调用父类构造方法，并传递参数self
        self.sno = sno
        self.mark = mark

    def getSno(self):
        return self.sno

    def getMark(self):
        return self.mark



class Teacher(UniversityMember):

    def __init__(self,name,age,tno,salary):
        UniversityMember.__init__(self,name,age)
        self.tno = tno
        self.salary = salary

    def getTno(self):
        return self.tno

    def getSalary(self):
        return self.salary



if __name__ == '__main__':
	student = Student('gavin',22,'111222211',100)
	print student.age
	print student.name
	print student.getAge()
	print student.getMark()