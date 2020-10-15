class Student:
    school = 'Python'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m2

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    '''def get_m1(self):  #getters
        return self.m1

    def set_m1(self):  #setters
        self.m1 = value'''
    @classmethod  #decorator
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is student class")

s1 = Student(34,67,45)
s2 = Student(36,29,76)

print(s1.avg())
print(Student.getSchool())

Student.info()