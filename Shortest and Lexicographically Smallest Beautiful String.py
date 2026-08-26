s = "0101111000101011001"
k = 9

if "1" not in s:
    #return ""
    print("empty")
 
result = ""
mini = 1000000
for i in range(len(s)):
    
    substr = ""
    for j in range(i):
        substr += s[j]
    
    if substr.count("1") == k and len(substr) < mini:
        mini = len(substr)
        while substr[-1] != "1":
            substr = substr[:-1]
        while substr[0] != "1":
            substr = substr[1:]
        
        result = substr
    
    substr2 = ""
    for l in range(i,len(s)):
        substr2 += s[l]
    if substr2.count("1") == k and len(substr2) < mini:
        mini = len(substr2)
        while substr2[-1] != "1":
            substr2 = substr2[:-1]
        while substr2[0] != "1":
            substr2 = substr2[1:]
    
        result = substr2
    #print(substr2)
    
        

print(result)        