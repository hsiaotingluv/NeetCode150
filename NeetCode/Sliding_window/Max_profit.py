import math

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min = math.inf
        max = 0
        curr_profit = 0
        max_profit = 0

        for price in prices:
            if price < min:
                min = price
            if price > min and price > max:
                max = price
                curr_profit = max - min
                max = 0
                if curr_profit > max_profit:
                    max_profit = curr_profit

        return max_profit

prices = [7,1,5,3,6,4]
prices = [7,6,5,4,3,2,1]
print(Solution().maxProfit(prices))



            