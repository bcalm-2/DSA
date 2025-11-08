class Solution:
    def replaceElements(self, arr):
        mx=-1
        for i in range(len(arr)-1,-1,-1):
            a=arr[i]
            arr[i]=mx
            if a>mx:
                mx=a
        return arr
        