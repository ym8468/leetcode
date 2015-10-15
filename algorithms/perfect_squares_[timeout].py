class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        squares = [1]
        i = 2
        square = i * i
        while square <= n:
            squares.append(square)
            i += 1
            square = i * i
        if square == n:
            return 1
        res = [0]
        res += [1] * n
        i = 2
        while i <= n:
            preKeys = []
            for square in squares:
                if square > i:
                    break
                elif square == i:
                    preKeys = []
                    break
                else:
                    preKeys.append(i - square)
            if not preKeys:
                res[i] = 1
            else:
                res[i] = min([res[key] for key in preKeys]) + 1
            i += 1
        return res[-1]
