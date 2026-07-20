# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Let's start with a placeholder node
        dummy = ListNode()

        # Build a new Linked List out of the dummy
        tail = dummy

        # Perform a traversal if neither list is empty
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                # Increment the list1 pointer
                list1 = list1.next
            else:
                tail.next = list2
                # Increment the list2 pointer
                list2 = list2.next

            # Increment tail one more time
            tail = tail.next
        
        # Now for the remaining values to append
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        # Returning dummy as it is a copy of tail
        # and meaningful data didn't get added
        # until the first tail.next
        return dummy.next