class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range (1,1000):
            x = k*i
            if x not in nums:
                return x        