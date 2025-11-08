class Solution:
    def leaders(self, arr):
        comp=arr[-1]
        i= len(arr)-2
        while i>=0:
            if arr[i] <comp:
                del arr[i]
                
            else:
                comp=arr[i]
                i=i-1
           
        return arr  