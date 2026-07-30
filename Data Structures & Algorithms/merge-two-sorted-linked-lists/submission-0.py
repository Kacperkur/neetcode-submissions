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

            # if the value in the first list is lower then append it to the dummy node
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            # otherwise append the value in list 2 to the node
            else:
                node.next = list2
                list2 = list2.next
            # then setup a blank new node for the next iteration
            node = node.next
        # when we hit the final one we appened the one with the last value
        node.next = list1 or list2
        # return the dummy head that points to the beginning of the sorted list
        return dummy.next
        