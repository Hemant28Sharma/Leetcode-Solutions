#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        smallest=prices[0]
        for i in prices:
            if i<smallest:
                smallest=i
            if i>smallest and profit < i-smallest:
                profit=i-smallest
        return profit