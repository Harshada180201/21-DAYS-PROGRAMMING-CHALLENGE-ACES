# 21-DAYS-PROGRAMMING-CHALLENGE-ACES
LEARNING PYTHON

# DAY_7

_1)LAMBDA FUNCTION_

A lambda function is a small anonymous function. A lambda functioncan 
take any number of arguments, but can only have one expression.
Lambda functions are used when you need a function for a short period of
time. This is commonly used when you want to pass a function as an
argument to higher-order functions, that is, functions that take other 
functions as their arguments.

_2)FILTER FUNCTION_

The filter() function returns an iterator were the items are filtered through a function to test 
if the item is accepted or not.
Syntax:
filter(function , <list type>)

_3)MAP FUNCTION_

The map() function iterates through all items in the given iterable and executes the function we passed as an argument on each of them.
The syntax is:
map(function, iterable(s))
We can pass as many iterable objects as we want after passing the function we want to use

_4)REDUCE FUNCTION_

reduce() works differently than map() and filter(). It does not return a new list based on the function and iterable we've passed. Instead, it returns a single value.
Also, in Python 3 reduce() isn't a built-in function anymore, and it can be found in the functools module.
The syntax is:
reduce(function, sequence[, initial])

