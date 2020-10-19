a = 5
b = 2
try:
    print("Resource Open")
    print(a/b)
    k = int(input("Enter the number:"))
    print(k)

except ZeroDivisionError as e:
    print("Hey,We cannot divide a number by zero", e)

except ValueError as e:
    print("Invalid input")

except Exception as e:
    print("Something went wrong")

finally:  #finally block will be executed if we get error as
          # well as if we don't get error
    print("Resource Close")

'''
OUTPUT: Resource Open
        2.5
        Enter the number:y
        Invalid input
        Resource Close
        
        Resource Open
        2.5
        Enter the number: 5
        5
        Resource Close
'''
