def binary_search(arr , target):
    n = len(arr)
    left = 0 
    right = n -1

    while left <= right:
        mid = ( left + right ) // 2 
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target :
            left = mid + 1 
        else :
            right = mid - 1 
    return -1

arr = [1,2,3,4,5,6,7,8,9,10]
index = print ("Element not found !") if (binary_search(arr , -1) == -1 ) else print (f"ELEMENT FOUND AT INDEX {binary_search(arr , -1)}")


            