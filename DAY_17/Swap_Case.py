'''Problem Statement: You are given a string and
your task is to swap cases. In other words, convert all
lowercase letters to uppercase letters and vice versa.'''

def swap_case(s):
    x = s.swapcase()
    return x

if __name__ == '__main__':
    s = input("Enter string: ")
    result = swap_case(s)
    print(result)

'''
OUTPUT: Enter string: Hello Geeks!
        hELLO gEEKS!
        
        Enter string: Swap cAse
        sWAP CaSE
'''