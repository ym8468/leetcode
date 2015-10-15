class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(2, n):
            if self.isPrime(i):
                count += 1
        return count
        
    def isPrime(self, n):
        if n < 2:
            return False
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True
