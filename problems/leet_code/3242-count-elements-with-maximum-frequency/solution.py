class Solution:
    def maxFrequencyElements(self, nums):
        d,m,c={},float('-inf'),0
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
            if d[nums[i]]>m:
                m=d[nums[i]]
        for i in d:
            if d[i]==m:
                c+=d[i]
        return c
