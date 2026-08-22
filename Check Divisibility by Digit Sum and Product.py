n = 99

result = False
n2 = []
n2 = [int(x) for x in str(n)]

Sum = sum(n2)
Prod = 1

for digit in n2:
    Prod *= digit
print(Sum,Prod)
if n % (Sum + Prod) == 0:
    result = True
print(result)
