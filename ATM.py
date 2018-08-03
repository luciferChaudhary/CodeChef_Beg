cash,bal = input().split()
cash = float(cash)
bal = float(bal)
if (cash%5)==0 and (bal-0.5)>=cash:
    bal = bal-0.5-cash
print(bal)

