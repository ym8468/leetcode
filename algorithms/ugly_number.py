class Solution:
    # @param {integer} num
    # @return {boolean}
    def isUgly(self, num):
        for i in [2,3,5]:
            while num % i == 0 < num:
                num /= i
        return num == 1
