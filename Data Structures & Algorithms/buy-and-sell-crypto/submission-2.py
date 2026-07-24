class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # make the min price the first in the list
        min_price = prices[0]
        ans = 0
        
        for i,price in enumerate(prices):
            # profit is the current iteration - minimum price
            profit = price - min_price
            # answer is either 0 if not profitable, or the best profit
            ans = max(ans,profit)
            # compare the current price to the min to see if it needs to be updated
            min_price = min(min_price, price)
        return ans