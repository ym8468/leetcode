class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.find('+ ') >= 0:
            return False
        if s.find(' e') >= 0:
            return False
        try:
            int(s)
            return True
        except:
            pass
        try:
            float(s)
            return True
        except:
            pass
        try:
            parse = s.split('e')
            if len(parse) != 2:
                raise
            x = int(parse[0])
            y = int(parse[-1])
            return True
        except:
            pass
        return False
