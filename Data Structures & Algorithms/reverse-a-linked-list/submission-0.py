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
        if not head:
            return None
            
        cur = head
        new_list = None
        
        while cur:
            # Create a new node that points to the previous "new_list"
            new_list = ListNode(cur.val, new_list)
            cur = cur.next
            
        return new_list

