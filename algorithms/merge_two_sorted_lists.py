# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        if l1.val > l2.val:
            head = l2
            l2 = l2.next
        else:
            head = l1
            l1 = l1.next
        merge = head
        while l1 and l2:
            if l1.val > l2.val:
                merge.next = l2
                l2 = l2.next
            else:
                merge.next = l1
                l1 = l1.next
            merge = merge.next
        merge.next = l1 or l2
        return head
