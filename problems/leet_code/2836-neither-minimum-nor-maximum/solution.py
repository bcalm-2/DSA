class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn = min(nums)
        mx = max(nums)
        for x in nums:
            if x != mn and x != mx:
                return x
        return -1
        
