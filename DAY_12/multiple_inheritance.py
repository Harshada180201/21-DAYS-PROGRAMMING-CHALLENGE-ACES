print("**MULTIPLE INHERITANCE**")
class A:
    def feature1(self):
        print("Features 1 working")

    def feature2(self):
        print("Features 2 working")

class B:
    def feature3(self):
        print("Features 3 working")

    def feature4(self):
        print("Features 4 working")

class C(A,B): #inherited from both class A and B
    def feature5(self):
        print("Features 5 working")

a1 = A()

a1.feature1()
a1.feature2()

b1 = B()

b1.feature3()

c1 = C()
c1.feature4()

'''
OUTPUT: **MULTIPLE INHERITANCE**
        Features 1 working
        Features 2 working
        Features 3 working
        Features 4 working
'''