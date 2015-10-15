class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = len(nums)
        if count <= 1:
            return
        cur = 0
        last = 0
        while cur < count:
            if nums[cur] != 0:
                nums[cur], nums[last] = nums[last], nums[cur]
                last += 1
            cur += 1
