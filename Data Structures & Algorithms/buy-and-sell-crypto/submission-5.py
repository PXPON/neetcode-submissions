class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Find the minimum and the maximum
        min = 100
        max = 0

        for price in prices:
            if price < min:
                min = price
            elif price - min > max:
                max = price - min

        return max

