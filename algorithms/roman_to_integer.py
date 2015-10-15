class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        romanNumMap = {}
        romanNumMap['I'] = 1
        romanNumMap['V'] = 5
        romanNumMap['X'] = 10
        romanNumMap['L'] = 50
        romanNumMap['C'] = 100
        romanNumMap['D'] = 500
        romanNumMap['M'] = 1000
        cmpFlg = False
        res = 0
        for i in s[::-1]:
            cur = i.upper()
            if cmpFlg and romanNumMap[cur] < romanNumMap[pre]:
                res -= romanNumMap[cur]
                cmpFlg = False
            else:
                res += romanNumMap[cur]
                pre = cur
                cmpFlg = True
        return res
