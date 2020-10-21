'''
Task:You are given the shape of the array in the form of space-separated
integers, each integer representing the size of different dimensions, your
task is to print an array of the given shape and integer type using the
tools numpy.zeros and numpy.ones.'''


import numpy
a = []
for x in input().split():
    a.append(int(x))

print(numpy.zeros(a, dtype = numpy.int))
print(numpy.ones(a, dtype = numpy.int))

'''OUTPUT:  2 2 2
            [[[0 0]
              [0 0]]

             [[0 0]
              [0 0]]]
            [[[1 1]
              [1 1]]

             [[1 1]
              [1 1]]]
'''