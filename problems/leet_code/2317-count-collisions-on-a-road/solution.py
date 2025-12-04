class Solution:
    def countCollisions(self, s):
        return len(s.lstrip('L').rstrip('R').replace('S',''))
