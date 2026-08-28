s = "baba"
target = "abba"
#output should be baab

letters = {}
length = len(s)

if length % 2 == 0: # it's an even sized word
    #storing their frequency
    for char in s: 
        if char not in letters.keys():
            letters[char] = 1
        else:
            letters[char] += 1
    
    #checking for  any letter with odd frequency
    for v in letters.values():
        if v % 2 != 0: 
            print("adios")
            #return ""
    
    dummy = ""
    for k in letters.keys():
        dummy += k
        for k2 in letters.keys():
            if k != k2:
                dummy += k2
                dummy += dummy[::-1]
                if dummy > target:
                    print(dummy)
                    #return target
        dummy = ""
            
else: # it's an odd sized word
    for char in s:
        if char not in letters.keys():
            letters[char] = 1
        else:
            letters[char] += 1
    
    

print(length)