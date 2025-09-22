def bubble_sort (arr):
    n = len(arr)
    for i in range(n):
        for j in range (n - i - 1 ):
            if arr[j] > arr [j+1] :
                arr[j] , arr[j+1] = arr[j+1] , arr[j]

arr = [6,2,4,7,8,5,3,2]
print ("Unsorted array : " , arr )
bubble_sort(arr)
print ("Sorted array : " , arr)