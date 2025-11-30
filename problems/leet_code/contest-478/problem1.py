class Solution(object):
    def countElements(self, nums, k):
        nums.sort()
        n = len(nums)
        greater_count = [0] * n
    
        for i in range(n - 2, -1, -1):
            if nums[i] == nums[i + 1]:
                greater_count[i] = greater_count[i + 1]
            else:
                greater_count[i] = n - (i + 1)
    
        greater_count[-1] = 0
    
        return sum(1 for g in greater_count if g >= k)

print(countElements([5,5,5], 1))
