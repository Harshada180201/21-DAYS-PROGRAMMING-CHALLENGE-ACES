pos = -1

def search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True

    return False


list = [5,8,4,6,9,2]
n = 9

if search(list, n):
    print("Found at ",pos)

else:
    print("Not Found")