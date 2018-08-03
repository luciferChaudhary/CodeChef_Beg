def fun(arr1,arr2):
    for x in range(arr1[1],arr1[2]):
        func = arr2[0]*x + arr2[1]
t = int(input())
for i in range(t):
    s1 = input()
    arr1 = s1.split()
    for j in range(arr1[0]):
        s2 = input()
        arr2 = s2.split()