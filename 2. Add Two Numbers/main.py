from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        residue = 0
        result_list = ListNode(0)
        current_item = result_list
        
        while l1 or l2 or residue:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            
            total = num1 + num2 + residue
            
            residue = total // 10
            new_num = total % 10
            
            current_item.next = ListNode(new_num)
            current_item = current_item.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None            
        
        return result_list.next
    
def list_to_linked(lst):
    dummy = ListNode(0)
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

l1 = list_to_linked([2,4,3])
l2 = list_to_linked([5,6,4])

result = Solution().addTwoNumbers(l1, l2)
current = result
while current:
    print(current.val, end=" ")  
    current = current.next
print()

# [2,4,3]
# [5,6,4]

# ===

# [7,0,8]