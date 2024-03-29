"""You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by 
splicing together the nodes of the first two lists.

Return the head of the merged linked list."""

class ListNode:
    """ Definition for singly-linked list."""
    def __init__(self,val=0, next= None):
        self.val = val
        self.next = next

def merge_lists(list1:ListNode , list2: ListNode) -> ListNode:
    """using pointers"""
    head = ListNode()
    current = head

    while list1 and list2:
        if list1.val < list2.val:# if the value of list1 is less than list2
            current.next = list1 # we add list1 to the current node
            list1 = list1.next # we move to the next node in list1
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # if one of the lists is empty, we add the other list
    if list1:
        current.next = list1
    if list2:
        current.next = list2
    return head.next

