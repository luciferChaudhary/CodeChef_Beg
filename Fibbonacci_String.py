def count(s):
    dict = {}
    k = dict.keys()
    for i in s:
        if i in k:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    return dict
def lt(ct):
    lst = list()
    for key,value in ct.items():
        lst.append(value)
        lst = sorted(lst, reverse = True)
    return lst
def formula(lst):
    if len(lst) < 3:
        return print('Dynamic')
    else:
        for i in range(0,(len(lst)-2)):
            for j in range(1,(len(lst)-1)):
                if lst[i] == (lst[j] + lst[j+1]):
                    return print('Dynamic')

    return print('Not')

t = int(input())
for i in range(t):
    s = input()
    ct = count(s)
    lst = lt(ct)
    formula(lst)