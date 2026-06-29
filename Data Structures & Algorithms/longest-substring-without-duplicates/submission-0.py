class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        result = set()
        maxL = 0
        for r in range(len(s)):
            while s[r] in result:
                result.remove(s[l])
                l += 1
            result.add(s[r])
            maxL = max(maxL , r - l + 1)
        return maxL