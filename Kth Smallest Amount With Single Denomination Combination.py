coins = [6,5]
k = 1435065516

coins = sorted(coins)
l = set()
i = 0
while(i <= k):
    i += 1
    for coin in coins:
        l.add(coin*i)
    
    

l = sorted(list(l))
print(l,l[k-1])