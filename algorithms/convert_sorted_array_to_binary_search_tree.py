# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        midIndex = len(nums)/2
        root = TreeNode(nums[midIndex])
        root.left = self.sortedArrayToBST(nums[0:midIndex])
        root.right = self.sortedArrayToBST(nums[midIndex+1:])
        return root
