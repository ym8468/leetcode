class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        if not root.left and not root.right:
            if root.val == sum:
                return [[root.val]]
            else:
                return []
        else:
            subResults = self.pathSum(root.left, sum-root.val)+self.pathSum(root.right, sum-root.val)
            return [[root.val]+subResult for subResult in subResults]
