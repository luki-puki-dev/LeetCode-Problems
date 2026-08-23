num = "9?"

if "?" not in num:
    num = list(map(int,str(num)))
    halfSize = len(num) // 2
    if sum(num[:halfSize]) == sum(num[-halfSize:]):
        print("false")
        #return False
    else:
        print("true")
        #return True
        
elif num.count("?") % 2 != 0:
        print("true")
        #return True
else:
    num = list(map(str,str(num)))
    halfSize = len(num) // 2
    questionMarksFirstHalf = num[:halfSize].count("?")
    questionMarksSecondHalf = num[halfSize:].count("?")
    sumFirstHalf = 0
    for item in num[:halfSize]:
        if item != "?":
            sumFirstHalf += int(item)
            
    sumSecondHalf = 0
    for item in num[halfSize:]:
        if item != "?":
            sumSecondHalf += int(item)
    if questionMarksFirstHalf > questionMarksSecondHalf:
        print("true - alice wins")
        #return True
    elif questionMarksFirstHalf == 0:
        
        if( sumFirstHalf - sumSecondHalf) == (9/2)*questionMarksSecondHalf:
            print("false - bob wins1")
            #return False
        elif (sumFirstHalf - sumSecondHalf) > (9/2)*questionMarksSecondHalf:
            print("true - alice wins")
            #return True
        elif (sumFirstHalf - sumSecondHalf) < (9/2)*questionMarksSecondHalf:
            print("true - alice wins")
            #return True
    elif questionMarksFirstHalf != 0:
        if (sumFirstHalf-sumSecondHalf)  == (9/2)*(questionMarksSecondHalf-questionMarksFirstHalf):
            print("false - bob wins2")
            #return False
        elif (sumFirstHalf-sumSecondHalf)  > (9/2)*(questionMarksSecondHalf-questionMarksFirstHalf):
            print("true - alice wins")
            #return True
        elif (sumFirstHalf-sumSecondHalf)  < (9/2)*(questionMarksSecondHalf-questionMarksFirstHalf):
            print("true - alice wins")
            #return true
