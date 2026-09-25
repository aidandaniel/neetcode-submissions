class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        totalS = 0
        totalT = 0
        for c in s:
            totalS += ord(c) **2
        for char in t:
            totalT += ord(char) **2 

        if totalS == totalT:
            return True
        else:
            return False