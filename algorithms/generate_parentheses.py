class Solution(object):
    def generateParenthesis(self, n, open=0):
        """
        :type n: int
        :rtype: List[str]
        """
        if n > 0 and open >= 0:
            return ['('+p for p in self.generateParenthesis(n-1, open+1)] + [')'+p for p in self.generateParenthesis(n, open-1)]
        return [')' * open] * (not n)
