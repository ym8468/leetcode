class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        tranversal = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                tranversal.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return tranversal[::-1]
