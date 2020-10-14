class Computer:
    def __init__(self):
        self.name = 'Harshada'
        self.age = 19

    def update(self):
        self.age = 20

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()
c1.age = 30
c1.name = 'Ravi'
c2 = Computer()

if c1.compare(c2):  #comparing
    print("They are same")
else:
    print("They are different")

#c1.update()
print(c1.name)
print(c2.name)
print(c1.age)
print(c2.age)

'''OUTPUT: 'They are different
            Ravi
            Harshada
            30
            19''