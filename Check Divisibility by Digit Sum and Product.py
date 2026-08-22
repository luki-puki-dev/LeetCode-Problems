class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = False
        n2 = []
        n2 = [int(x) for x in str(n)]
        Sum = sum(n2)
        Prod = 1
        for digit in n2:
            Prod *= digit
        if n % (Sum + Prod) == 0:
            result = True
        return result
        
        