# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if not head:
            return head
        curNode = head
        while(curNode.next):
            if curNode.next.val == curNode.val:
                curNode.next = curNode.next.next
            else:
                curNode = curNode.next
        return head
