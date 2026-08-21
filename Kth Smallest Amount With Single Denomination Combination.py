
coins = [4,8]
k = 55789

coins = sorted(coins)
l = set()
i = 0
req = coins[-1] ** coins[0]
while(True):
    i += 1
    for coin in coins:
        l.add(coin*i)
    
    if len(l) >= k and i > req:
        break

l = sorted(list(l))
print(l,l[k-1])

5, 10, 15, 20, 25, 30, 35
2, 4, 6, 8, 10, 12, 14

2, 4, 5, 6, 8, 10, 12, 14, 15