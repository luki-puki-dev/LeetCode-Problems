num = "5023??"

if "?" not in num:
    num = list(map(int,str(num)))
    halfSize = len(num) // 2
    if sum(num[:halfSize]) == sum(num[-halfSize:]):
        print("false")
    else:
        print("true")
        
elif num.count("?") % 2 != 0:
        print("false")
    



