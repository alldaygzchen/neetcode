# merge k nodes every time with a node #0(k*n)
# merge k nodes with merge sort technique #0(logk*n)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):

        if not lists or len(lists) ==0:
            return None

        while len(lists)>1:
            mergedLists = []
            
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1)<len(lists) else None

                mergedLists.append(self.mergelist(l1,l2))
            lists = mergedLists
        return lists[0]


    def mergelist(self,l1,l2):
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next =l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next =l1
        if l2:
            tail.next =l2
        return dummy.next

s =Solution()
print(s.mergeKLists([]))