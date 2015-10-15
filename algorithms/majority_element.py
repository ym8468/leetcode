class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        me = nums[-1]
        cnt = 1
        halfLen = len(nums)>>1
        for i in nums[0:-1]:
            if cnt == 0:
                me = i
            if i == me:
                cnt += 1
                if cnt > halfLen:
                    return me
            else:
                cnt -= 1
        return me
