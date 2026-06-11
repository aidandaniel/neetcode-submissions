class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        a1 = sorted(s)
        a2 = sorted(t)
        if len(s) != len(t):
            return False
        for i in range(len(a1)):
            if a1 == a2:
                return True
        return False