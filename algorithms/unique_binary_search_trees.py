class Solution:
    # @param {integer} n
    # @return {integer}

    def numTrees(self, n):
        if n <= 0:
            return 0
        cntMap = {}
        cntMap[0] = 1
        for i in range(1, n+1):
            cnt = 0
            for j in range(1, i+1):
                cnt += cntMap[j-1] * cntMap[i-j]
            cntMap[i] = cnt
        return cntMap[n]
