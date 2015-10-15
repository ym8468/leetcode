class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n <= 1:
            return 1
        resT = [1] * n
        for i in range(2, n):
            resT[i] = resT[i-1] + resT[i-2]
        return resT[n-2] + resT[n-1]
