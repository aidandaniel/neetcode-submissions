class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxGain = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                p = prices[r] - prices[l]
                maxGain = max(maxGain, p)
            else:
                l = r
            r += 1
        return maxGain
        