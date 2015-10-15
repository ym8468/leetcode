class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        front = 0
        back = len(nums) - 1
        cur = front
        while cur <= back:
            while nums[cur] == 2 and cur < back:
                nums[cur], nums[back] = nums[back], nums[cur]
                back -= 1
            while nums[cur] == 0 and cur > front:
                nums[cur], nums[front] = nums[front], nums[cur]
                front += 1
            cur += 1
