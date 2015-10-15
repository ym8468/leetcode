class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        pre = prices[0]
        min = pre
        maxP = 0
        for cur in prices[1:]:
            if cur < min:
                min = cur
            elif cur > pre:
                curP = cur - min
                maxP = max(curP, maxP)
            pre = cur
        return maxP
