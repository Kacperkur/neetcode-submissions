class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        ans = 0
        
        for i,price in enumerate(prices):
            profit = price - min_price
            ans = max(ans,profit)
            min_price = min(min_price, price)
        return ans