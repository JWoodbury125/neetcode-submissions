class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = float("-inf")
        l = 0
        for r in range(len(prices)):
            if r > 0 and prices[r] < prices[l]:
                l = r
            maxprofit = max(maxprofit, prices[r] - prices[l])

        return 0 if maxprofit == float("-inf") else maxprofit

            