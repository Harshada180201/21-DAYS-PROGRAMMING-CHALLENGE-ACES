class Computer:
    def config(self):
        print("This is i5,16gb,1TB Laptop")


comp1 = Computer()
comp2 = Computer()

Computer.config(comp1)
Computer.config(comp2)

'''OUTPUT: This is i5,16gb,1TB Laptop
           This is i5,16gb,1TB Laptop'''

comp1.config()
comp2.config()

'''OUTPUT: This is i5,16gb,1TB Laptop
           This is i5,16gb,1TB Laptop'''