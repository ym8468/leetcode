# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)

    def merge(self, l, r):
        if not l or not r:
            return l or r
        if l.val > r.val:
            head = r
            r = r.next
        else:
            head = l
            l = l.next
        merged = head
        while l and r:
            if l.val > r.val:
                merged.next = r
                r = r.next
            else:
                merged.next = l
                l = l.next
            merged = merged.next
        merged.next = l or r
        return head
