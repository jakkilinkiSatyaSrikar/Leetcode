# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        vals = []
        f_part = []
        #s_part = []
        length = 0
        itr = head
        while itr:
            length +=1
            itr= itr.next
        c = 1
        half = length/2
        itr = head
        b2f = -1
        while itr:
            if c<=half:
                f_part.append(itr.val)
                #itr = itr.next
            else:
                vals.append(itr.val + f_part[b2f])
                b2f -=1
            c +=1
            itr = itr.next
            #print(f_part)
        return (max(vals))