''' Inheritance: using features of existing class
Single and multilevel inheritance'''

class A:  #Super Class
    def feature1(self):
        print("Features 1 working")

    def feature2(self):
        print("Features 2 working")

class B(A):  #Sub Class : it can access all the features of super class
    def feature3(self):
        print("Features 3 working")

    def feature4(self):
        print("Features 4 working")

class C(B):
    def feature5(self):
        print("Features 5 working")

a1 = A()

a1.feature1()

b1 = B()

b1.feature2()

c1 = C()

c1.feature3()
c1.feature5()

'''
OUTPUT: Features 1 working
        Features 2 working
        Features 3 working
        Features 5 working


'''