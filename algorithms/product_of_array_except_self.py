class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        p1 = [1 for i in nums]
        p2 = [1 for i in nums]
        res = [1 for i in nums]
        end = len(nums) - 1
        for i in range(1, len(nums)):
            p1[i] = nums[i-1] * p1[i-1]
            p2[end-i] = nums[end-i+1] * p2[end-i+1]
        for i in range(0, len(nums)):
            res[i] = p1[i] * p2[i]
        return res
