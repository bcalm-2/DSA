class Solution:
    def getSneakyNumbers(self, nums):
        visited = set()

        result = []
        for num in nums:
            if(num not in visited):
                visited.add(num)
            else:
                result.append(num)

        return result
