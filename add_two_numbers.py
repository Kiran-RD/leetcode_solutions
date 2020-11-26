# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ll1 = l1
        ll2 = l2
        l3 = ll3 = None
        carry_over = 0
        while True:
            if ll1 is not None or ll2 is not None:
                if ll1 is None:
                    digit_sum = ll2.val+carry_over
                elif ll2 is None:
                    digit_sum = ll1.val+carry_over
                else:
                    digit_sum = ll1.val+ll2.val+carry_over
                #print(n1,n2,digit_sum)
                tens = digit_sum//10
                units = digit_sum%10
                if not ll3:
                    ll3 = ListNode(val=units,next=None)
                    l3 = ll3
                else:
                    ll3.next = ListNode(val=units,next=None)
                    ll3 = ll3.next
                carry_over = tens
                if ll1:
                    ll1 = ll1.next
                if ll2:
                    ll2 = ll2.next
            else:
                break
        
        if carry_over:
            ll3.next = ListNode(val=carry_over,next=None)
                
        return l3
