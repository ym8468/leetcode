class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        primeFlgs = [True for i in range(0, n)]
        primeFlgs[0], primeFlgs[1] = False, False
        i = 2
        while i*i < n:
            if not primeFlgs[i]:
                i += 1
                continue
            j = i*i
            while j < n:
                primeFlgs[j] = False
                j += i
            i += 1
        count = 0
        for flg in primeFlgs:
            if flg:
                count += 1
        return count
