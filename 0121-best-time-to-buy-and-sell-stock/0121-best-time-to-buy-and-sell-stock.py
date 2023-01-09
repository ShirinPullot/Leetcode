class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy=0
        sell=1
        while sell<len(prices):
            current_profit=prices[sell]-prices[buy]
            if prices[buy]<prices[sell]:
                max_profit= max(current_profit,max_profit)
                sell+=1
            else:
                buy=sell
                sell+=1
        return max_profit
        