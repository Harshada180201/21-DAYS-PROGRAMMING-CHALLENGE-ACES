class Student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.brand = 'DELL'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = Student('Harshada',26,)
s2 = Student('Trupti',18)

s1.show()

'''
OUTPUT: Harshada 26
        DELL i5 8
'''
