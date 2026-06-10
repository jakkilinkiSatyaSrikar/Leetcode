# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li = []
        count = -1
        itr = head
        while itr:
            li.append(itr.val)
            itr = itr.next
        #li.reverse()
        print(li)
        itr = head
        while itr:
            itr.val = li[count]
            count = count-1
            itr = itr.next
        return head