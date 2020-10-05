'''
                        ***Task***
Given an integer,n, perform the following conditional actions:

1.If n is odd, print Weird
2.If n is even and in the inclusive range of 2 to 5, print Not Weird
3.If n is even and in the inclusive range of 6 to 20, print Weird
4.If n is even and greater than 20, print Not Weird'''


#Implementation

n = int(input("Enter the number: "))
if n % 2 == 1:
    print("Weird")

elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")

elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")

else:
    print("Not Weird")


'''
OUTPUT : 
Enter the number: 35
Weird

enter any integer number and check
'''