def bubbleSort(arr):
   n = len(arr)
   # Traverse through all array elements
   for i in range(n):
   # Last i elements are already in correct position
        for j in range(0, n-i-1):
      # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [64,23,56,21,10,15]
print("Given Array is: ",arr)
bubbleSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
   print (arr[i])


'''
OUTPUT : 
Given Array is:  [64, 23, 56, 21, 10, 15]
Sorted array is:
10
15
21
23
56
64
'''

