print("////////////////////////////////")
print("             for loop           ")
print("////////////////////////////////")
# Program to print squares of all numbers present in a list

numbers = [1, 2, 4, 6, 11, 20]

sq = 0

for val in numbers:
    # calculating square of each number
    sq = val * val
    print(sq)

print()
print("////////////////////////////////")
print("           while loop           ")
print("////////////////////////////////")

print()
print("1.While loop")
num = 1
# loop will repeat itself as long as
# num < 10 remains true
while num < 10:
    print(num)
    #incrementing the value of num
    num = num + 3
print()
print("2.Nested while loop")
i = 1
j = 5
while i < 4:
    while j < 8:
        print(i, ",", j)
        j = j + 1
        i = i + 1

print()
'''print("3.Infinite while loop")
num = 1
while num<5:
   print(num)
'''

#************OUTPUT*******************
'''
////////////////////////////////
             for loop           
////////////////////////////////
1
4
16
36
121
400

////////////////////////////////
           while loop           
////////////////////////////////

1.While loop
1
4
7

2.Nested while loop
1 , 5
2 , 6
3 , 7

3.Infinite while loop will print 1 indefinitely because inside loop we are 
not updating the value of num, so the value of num will always remain 1 
and the condition num < 5 will always return true.
'''