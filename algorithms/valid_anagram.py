class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        cnts = {}
        for i in s:
            if i in cnts:
                cnts[i] += 1
            else:
                cnts[i] = 1
        for i in t:
            if i in cnts:
                cnts[i] -= 1
            else:
                return False
        for i in cnts:
            if cnts[i] != 0:
                return False
        return True
