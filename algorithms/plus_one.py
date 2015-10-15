class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        res = [i for i in digits]
        if digits[-1] < 9:
            res[-1] += 1
        else:
            res[-1] = 0
            for index in range(len(res)-2,-1,-1):
                if res[index] < 9:
                    res[index] += 1
                    break
                res[index] = 0
            if not res[0]:
                res = [1] + res
        return res
