n,k = input().split()
n = int(n)
k = int(k)
count = 0
while n>0:
    t = int(input())
    n = n-1
    if t%k==0:
        count = count +1
print(count)
