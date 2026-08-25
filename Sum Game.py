class Solution(object):
    def sumGame(self, num):

        if num.count("?") % 2 != 0:
            return True
            

        num = list(str(num))
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
        if (sumFirstHalf - sumSecondHalf) == 4.5 * (questionMarksSecondHalf - questionMarksFirstHalf):
            return False
        else:
            return True