def linearsearch(arr,n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i
    return -1

lst = [1,2,3,4,5]
x = linearsearch(lst,9)
if x==-1:
    print('Not Found')
else:
    print('found at',x+1)