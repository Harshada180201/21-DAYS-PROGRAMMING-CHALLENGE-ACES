'''a generator is a function that returns an object
(iterator) which we can iterate over (one value at a time)
A return statement terminates a function entirely,
yield statement pauses the function saving all its states
and later continues from there on successive calls.
'''

def Top():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n +=1


values = Top()

for i in values:
    print(i)

'''
OUTPUT: 1
        4
        9
        16
        25
        36
        49
        64
        81
        100
'''