class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        maxSum = nums[0]
        cur = nums[0]
        pre = nums[0]
        for i in nums[1:len(nums)]:
            if pre > 0:
                cur = pre + i
            else:
                cur = i
            maxSum = max(maxSum, cur)
            pre = cur
        return maxSum
