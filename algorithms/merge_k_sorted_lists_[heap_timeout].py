# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def precDown(self, lists, i=0):
        lchild = i*2 + 1
        rchild = lchild + 1
        while rchild < len(lists) or lchild < len(lists):
            if lists[lchild] != lists[-1] and lists[rchild].val < lists[lchild].val:
                child = rchild
            else:
                child = lchild
            if lists[i].val > lists[child].val:
                lists[i], lists[child] = lists[child], lists[i]
                i = child
                lchild = i*2 + 1
                rchild = lchild + 1
            else:
                break
     
    def buildHeap(self, lists):
        lists = filter(None, lists)
        start = len(lists)/2 -1
        for i in range(start, -1, -1):
            self.precDown(lists, i)
        return lists
        
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not filter(None, lists):
            return []
        lists = self.buildHeap(lists)
        head = lists[0]
        cur = head
        curLen = len(lists)
        lists[0] = lists[0].next
        while True:
            if lists[0] is None:
                lists = self.buildHeap(lists)
            else:
                lists = self.precDown(lists, 0)
            if not lists:
                break
            cur.next = lists[0]
            lists[0] = lists[0].next
            cur = cur.next
        return head
