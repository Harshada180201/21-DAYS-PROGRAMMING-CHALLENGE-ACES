def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        left = arr[:mid]  # Dividing the array elements
        right = arr[mid:]  # into 2 halves

        mergeSort(left)  # Sorting the first half
        mergeSort(right)  # Sorting the second half

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# printing the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


arr = [12, 11, 13, 5, 6, 7]
print("Given array is: ")
printList(arr)
mergeSort(arr)
print("Sorted array is: ")
printList(arr)

'''
OUTPUT: Given array is: 
        12 11 13 5 6 7 
        Sorted array is: 
        5 6 7 11 12 13
'''

