# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = []
        even = []
        
        itr = head
        count = 0
        while itr:
            if count%2 == 0:
                odd.append(itr.val)
            else:
                even.append(itr.val)
            itr = itr.next
            count = count +1
        odd.extend(even)
        #print(odd)
        itr = head
        count = 0
        while itr:
            #print(count)
            itr.val = odd[count]
            count = count + 1
            itr = itr.next
            #print(head)
        return head