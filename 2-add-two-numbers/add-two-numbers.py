# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = head = ListNode(0)

        up = 0
        while l1 and l2 :
            s = l1.val + l2.val + up
            up = s // 10
            head.next = ListNode(s % 10)
            l1 = l1.next
            l2 = l2.next
            head = head.next
        
        while l1 :
            s = l1.val + up
            up = s // 10
            head.next = ListNode(s % 10)
            l1 = l1.next
            head = head.next

        while l2 :
            s = l2.val + up
            up = s // 10
            head.next = ListNode(s % 10)
            l2 = l2.next
            head = head.next
        
        if up == 1 :
            head.next = ListNode(1)
        
        return answer.next   