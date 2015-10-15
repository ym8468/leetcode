class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        if not str:
            return 0
        s = ''
        str = str.strip()
        if str[0] == '-' or str[0] == '+':
            s = str[0]
            str = str[1:]
        for i in str:
            if i > '9' or i < '0':
                break
            s += i
        try:
            res = int(s)
            if res > 2147483647:
                return 2147483647
            if res < -2147483648:
                return -2147483648
            return res
        except:
            return 0
