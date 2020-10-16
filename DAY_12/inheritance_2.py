#Constructor in Inheritance
'''
when you create object of syb class it will call init of sub class first
If you have call super then it will 1st call init of Super class then call init of
sub class
'''
class A:

    def __init__(self):
        print("In A init")

    def feature1(self):
        print("Features 1-A working")

    def feature2(self):
        print("Features 2 working")

class B:

    def __init__(self):
        #super().__init__()  #trying to call __init__ method of A
        print("In B init")

    def feature1(self):
        print("Features 1-B working")

    def feature4(self):
        print("Features 4 working")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("In C init")

    def feature(self):
        super().feature2()
a1 = C()

a1.feature2()

'''Method Resolution Order(MRO)'''
