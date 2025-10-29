class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = 0
        output = []
        for num in nums:
            sum += num
            output.append(sum)
        return output
        
