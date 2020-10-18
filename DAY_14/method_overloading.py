'''Two methods with same name but different parameteresis method overloading'''
class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a = None,b=None,c=None):
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a
        return s

s1 = Student(58,69)
print(s1.sum(5,9,6))
print(s1.sum(5,9))
print(s1.sum(5))

'''
OUTPUT: 20
        14
        5
'''