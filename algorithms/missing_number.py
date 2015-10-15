class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        i = 0
        for num in nums:
            res ^= num
            res ^= i
            i += 1
        res ^= i
        return res
