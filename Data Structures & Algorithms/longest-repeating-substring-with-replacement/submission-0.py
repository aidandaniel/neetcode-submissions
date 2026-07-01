class Solution:
    from collections import defaultdict

    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = defaultdict(int)
        res = 0
        maxFreq = 0

        for right in range(len(s)):
            
            count[s[right]] += 1
            maxFreq = max(maxFreq, count[s[right]])
            while (right - l + 1) - maxFreq> k:
                count[s[l]] -= 1
                l += 1

            res = max(res, right - l + 1, )
        return res