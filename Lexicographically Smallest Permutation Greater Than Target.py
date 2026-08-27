from itertools import permutations
s = "leet"
target = "code"
result = ""
permutation = permutations(s)
for i in sorted(permutation):
    x = "".join(i)
    if x > target:
        result = x
        break
    
print(result)

# s[i]  s[i+1:]    s[:0+i]