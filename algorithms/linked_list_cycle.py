# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        slow = head
        fast = head
        while fast:
            if not fast.next:
                return False
            else:
                fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True
        return False
