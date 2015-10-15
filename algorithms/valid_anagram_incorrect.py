class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        res = 0
        for i in s:
            res ^= ord(i)
        for i in t:
            res ^= ord(i)
        return res == 0
