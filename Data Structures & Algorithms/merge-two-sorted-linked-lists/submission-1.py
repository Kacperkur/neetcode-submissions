# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = node = ListNode()

        # while there are still nodes to traverse in both lists
        while list1 and list2:

            # if the value in the first list is lower then append it to the current tail
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            # otherwise append the value in list 2 to the node
            else:
                node.next = list2
                list2 = list2.next
            # then advance to the newly attached node so it is ready to be a tail
            node = node.next
        # Once one list is exhausted we attatch the remainder of either list
        node.next = list1 or list2
        # return the dummy.next that points to the head of the sorted list
        return dummy.next
        