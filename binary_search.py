def binarysearch(arr,n):
    beg = 0
    end = len(arr)-1

    while beg <= end:
        mid = (beg + end) // 2
        if arr[mid] == n:
            return mid
        if arr[mid] > n:
            end = mid - 1
        if arr[mid] < n:
            beg = mid + 1
    return -1
lst = [2,4,6,8,10]
x = binarysearch(lst,8)
if x == -1:
    print('Not Found')
else:
    print('Found At',x+1)
