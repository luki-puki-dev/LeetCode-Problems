coins = [4,8]
k = 55789

result = 0
l = []
i = 0
while(True):
    i += 1
    for coin in coins:
       if (coin * i) not in l:
           l.append(coin*i)
    
    if len(l) >= k:
        break

l = sorted(l)
print(l[k-1])