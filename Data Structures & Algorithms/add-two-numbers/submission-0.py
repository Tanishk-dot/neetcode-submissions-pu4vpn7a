# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        str1 = ""
        str2 = ""
        while l1:
            str1 += str(l1.val)
            l1 = l1.next

        while l2:
            str2 += str(l2.val)
            l2 = l2.next

        
        str1 = str1[::-1]
        str2 = str2[::-1]
        val = int(str1) + int(str2)
        if val == 0:
            return ListNode(0)
        while val > 0:
            digit = val % 10
            curr.next = ListNode(digit)

            curr = curr.next
            val= val // 10

        return dummy.next
            


        