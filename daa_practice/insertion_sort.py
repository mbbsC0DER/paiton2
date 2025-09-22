#INSERTION SORT 

def insertion_sort(arr):
    for i in range (1 , len(arr)):
        key = arr[i]
        j = i - 1 
        
        while j >= 0 and key < arr[j]:
            arr[j + 1 ] = arr[j]
            j -= 1 
        arr[j+1] = key 

# def display(arr):
#     for i in arr :
#         print (i , end = " ")

arr = [4,2,7,3,1,6 , 2]
print ("Unsorted array : " , arr )
insertion_sort(arr)
print ("Sorted array : " , arr)
