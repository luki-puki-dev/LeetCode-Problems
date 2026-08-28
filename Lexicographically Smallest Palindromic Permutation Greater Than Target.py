s = "aaabbbb"
target = "abaaaaa"
#output should be aca

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
    nr_of_letters = 0
    for k,v in letters.items():
        nr_of_letters += 1
        if v % 2 != 0: 
            print("adios")
            #return ""
    if nr_of_letters == 1:
        if s > target:
            print(s)
            #return s
    
    dummy = ""
    for k,v in letters.items():
        dummy += (k*(v//2))
        for k2,v2 in letters.items():
            if k != k2:
                dummy += (k2*(v2//2))
                dummy += dummy[::-1]
                if dummy > target and (len(dummy) == len(target)):
                    print(dummy)
                    #return target
        dummy = ""
    print (dummy)
    #return ""

        
else: # it's an odd sized word
    for char in s:
        if char not in letters.keys():
            letters[char] = 1
        else:
            letters[char] += 1
    
    counter = 0
    middle = ""
    freq_middle = 0
    nr_of_letters = 0
    for k,v in letters.items():
        nr_of_letters += 1
        if v % 2 != 0:
            middle = k
            freq_middle = v
            counter += 1
            if counter >  1: # we need only one letter with odd frequency
                #return ""
                print(k,v)
    if nr_of_letters == 1:
        if s > target:
            print(s)
            #return s
    
    dummy = ""
    for k,v in letters.items():
        dummy += (k*(v//2))
        for k2,v2 in letters.items():
            if k != k2:
                if k2 == middle:
                    dummy += (middle*(freq_middle))
                    dummy += dummy.split(middle)[0]
                    print(dummy)
                else:
                    dummy += (k2*(v2//2))
                    dummy += dummy[::-1]
                    print(dummy)
                if dummy > target and (len(dummy) == len(target)):
                    print(dummy)
                    #return target
        dummy = ""

    #return ""

