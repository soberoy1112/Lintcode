class Solution:
    """
    @param: prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        deal = []
        if len(prices) == 0 or len(prices) == 1:
            return 0
        for i in range(1, len(prices)):
            deal.append(max(prices[i:]) - min(prices[:i]))
        if max(deal) > 0:
            return max(deal)
        else:
            return 0 
x = Solution()
print(x.maxProfit([3,2,3,1,2]))