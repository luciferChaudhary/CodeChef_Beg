cash = float(input())
bal = float(input())
if cash%5==0 and (bal+0.5)>=cash:
    bal = bal - 0.5 - cash
print(bal)
