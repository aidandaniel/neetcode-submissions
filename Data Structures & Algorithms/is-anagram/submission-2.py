class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sum = 0
        sum2 = 0
        for index, char in enumerate(s):
            sum += ord(char)**2
        for j, c in enumerate(t):
            sum2 += ord(c)**2

        if sum == sum2:
            return True
        else: return False

            