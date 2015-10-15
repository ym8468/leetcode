class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        start = 0
        end = len(nums) - 1
        mid = (start + end) / 2
        while start < end:
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                start = mid + 1
            else:
                end = max(mid - 1, start)
            mid = (start + end) /2
        if target <= nums[mid]:
            return mid
        return mid + 1
