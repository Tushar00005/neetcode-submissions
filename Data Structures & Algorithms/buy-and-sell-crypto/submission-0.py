class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices=prices[0]
        max_profit=0
        for i in range(len(prices)):
            if min_prices>prices[i]:
                min_prices=prices[i]
            else:
                profit=prices[i]-min_prices
                max_profit=max(max_profit,profit)
        return max_profit