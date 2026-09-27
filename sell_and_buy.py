class Solution(object):
    def maxProfit(self, prices):

        smallest = prices[0]
        max_profit = 0

        for i in prices:
            if i < smallest:
                smallest = i

            profit = i - smallest

            if profit > max_profit:
                max_profit = profit

        return max_profit