# Greedy Algorithm
class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        profit = 0
        for i in range(0, len(prices)-1):
            if prices[i] < prices[i + 1]:
                profit = profit + (prices[i+1]-prices[i])
        return profit