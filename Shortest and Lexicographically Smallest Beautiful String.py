s = "0101111000101011001"
k = 9

ones = [i for i, c in enumerate(s) if c == '1']
if len(ones) < k:
    #return ""
    print("none")
    
best = None
for i in range(len(ones) - k + 1):
    start, end = ones[i], ones[i + k - 1]
    candidate = s[start:end + 1]
    if best is None or len(candidate) < len(best) or (len(candidate) == len(best) and candidate < best):
        best = candidate
#return best

print(best)
    