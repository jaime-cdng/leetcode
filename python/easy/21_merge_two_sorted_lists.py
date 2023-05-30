"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        values = []
        while list1 is not None:
            values.append(list1.val)
            list1 = list1.next

        while list2 is not None:
            values.append(list2.val)
            list2 = list2.next

        sorted_values = sorted(values)


if __name__ == "__main__":
    solution = Solution()
    list1 = ListNode(1)
    list1.next = ListNode(3)
    list1.next.next = ListNode(2)
    list1.next.next.next = ListNode(4)

    list2 = ListNode(5)
    list2.next = ListNode(15)
    list2.next.next = ListNode(10)

    solution.mergeTwoLists(list1, list2)
