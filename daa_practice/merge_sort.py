
def merge_sort(arr):
    n = len(arr)
    c = []
    if n==1 :
        return arr
    # a = n //2 , b = n - (n // 2 )
    a = [] 
    b = []
    # while k < n//2 :
    #     a.append(arr[x])
    #     k += 1 
    #     x += 1 
    # while l < (n - (n//2)):
    #     b.append (arr[x])
    #     l+=1
    #     x+=1
    mid = n // 2 
    a = arr[ : mid ]
    b = arr[ mid : ]

    a = merge_sort(a)
    b = merge_sort(b)

    i = 0 
    j = 0 
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1 
            
        else :
            c.append(b[j])
            j += 1 
    while i < len(a):
        c.append(a[i])
        i += 1 
    while j < len(b):
        c.append (b[j])
        j += 1 
    return c 


arr = [2,3,4,6,7,4,3,1,2,4,5,6,0]
ans = merge_sort(arr)
print (ans )