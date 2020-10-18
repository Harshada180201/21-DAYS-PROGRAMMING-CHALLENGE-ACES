#creating iterator

class top:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

values = top()

print(next(values))

for i in values:
    print(i)

'''
OUTPUT: 1
        2
        3
        4
        5
        6
        7
        8
        9
        10
'''
