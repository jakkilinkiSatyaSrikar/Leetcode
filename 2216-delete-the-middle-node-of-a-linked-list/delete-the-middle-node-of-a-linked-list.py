# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr = head
        length = 0
        while itr:
            length = length+1
            itr = itr.next
        #length = length+1
        print(length)
        count = 0
        itr = head
        while itr.next:
            print(count)
            if count == (length//2)-1:
                itr.next = itr.next.next
                return head
            itr = itr.next
            count = count+1
        