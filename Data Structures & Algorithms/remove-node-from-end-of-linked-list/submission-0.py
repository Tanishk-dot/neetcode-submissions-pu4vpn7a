# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count += 1
        val = count - n
        prev = None
        current = head
        if val == 0:
            return head.next
        while val > 0:
            prev = current
            current = current.next
            val -= 1
        prev.next = current.next
        current.next = None
        return head


        