'''Given an integer n and n space-separated
integers as input create a tuple t of those n integers.
Then compute and print the result of hash(t)'''

n = int(input())
input_line = input()
input_list = input_line.split()
for i in range(n):
    input_list[i] = int(input_list[i])
t = tuple(input_list)
print(hash(t))

'''
OUTPUT: 2
        1 2
        -3550055125485641917
'''

'''
The hash() method returns the hash value of an object
if it has one. Hash values are just integers that are 
used to compare dictionary keys during a dictionary 
lookup quickly.
'''