class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0

        for i in range(1, n):
            current_profit = prices[i] - prices[i - 1]
            if current_profit > 0:
                ans += current_profit

        return ans
            
        