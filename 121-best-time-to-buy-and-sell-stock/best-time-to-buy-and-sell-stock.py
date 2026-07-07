class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_price = prices[0]
        ans = 0

        for i in range (1,n):  # since first day is the day u bought the stock
            curr_profit = prices[i] - min_price
            ans = max(curr_profit, ans)
            min_price = min(min_price, prices[i])
        return ans
              

                                                             

        