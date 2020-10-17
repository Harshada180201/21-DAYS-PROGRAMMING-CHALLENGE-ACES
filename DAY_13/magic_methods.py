a = 5
b = 6

c = 'Hello'
d = 'World'

print(a+b)
print(c+d)

print(int.__add__(a,b))
print(str.__add__(c,d))

'''
OUTPUT: 11
        HelloWorld
        11
        HelloWorld
'''