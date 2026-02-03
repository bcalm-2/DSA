class Solution:
    def isTrionic(self, nums):
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                if count == 0 or count == 1:
                    count = 1
                elif count == 2 or count == 3:
                    count = 3
                else:
                    count = 4
            elif nums[i] > nums[i + 1]:
                if count == 1 or count == 2:
                    count = 2
                elif count == 0 or count == 3:
                    return False
            else:
                return False

        return count == 3
