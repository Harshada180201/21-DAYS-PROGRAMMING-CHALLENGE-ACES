class Car:
    wheels = 4

    def __init__(self):
        self.mil = 10
        self.com = 'BMW'

c1 = Car()
c2 = Car()

c1.mil = 8
Car.wheels = 5

print("CAR:",c1.com," MILEAGE:",c1.mil,"  No. of Wheels:",c1.wheels)
print("CAR:",c2.com," MILEAGE:",c2.mil," No. of Wheels:",c2.wheels)

'''
OUTPUT: 
CAR: BMW  MILEAGE: 8   No. of Wheels: 5
CAR: BMW  MILEAGE: 10  No. of Wheels: 5
'''