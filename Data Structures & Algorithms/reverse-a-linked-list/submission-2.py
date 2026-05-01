class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head in None:
#             return head
        
#         cur = head
#         prev = None

#         while cur:
#             next_node = cur.next
#             next_node.next = cur


#             cur = cur.next

    
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt
            
        return prev
