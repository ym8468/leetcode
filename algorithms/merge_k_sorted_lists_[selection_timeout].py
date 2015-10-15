# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getMinIndex(self, lists):
        vals = []
        for i in range(0, len(lists)):
            val = lists[i].val if lists[i] else None
            vals.append(val)
        minVal = min([node.val for node in filter(None, lists)])
        return vals.index(minVal)

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not filter(None, lists):
            return []
        index = self.getMinIndex(lists)
        head = lists[index]
        lists[index] = lists[index].next
        cur = head
        while filter(None, lists):
            index = self.getMinIndex(lists)
            cur.next = lists[index]
            lists[index] = lists[index].next
            cur = cur.next
        return head
