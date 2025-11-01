class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) + 1
        for num in range(0, n):
            if num not in nums:
                return num

