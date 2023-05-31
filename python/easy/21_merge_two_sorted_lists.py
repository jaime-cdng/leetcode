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

        values.sort()

        node = ListNode()
        first = node

        for index, val in enumerate(values):
            node.val = val
            if index + 1 == len(values):
                break
            node.next = ListNode()
            node = node.next

        return first

    def mergeTwoListsOpt2(self, list1, list2):
        """
        Solution from another LeetCode user to compare performance.

        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return dummy.next

    def mergeTwoListsRescursive(self, list1, list2):
        """
        Solution from another LeetCode user to compare performance.

        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoListsRescursive(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoListsRescursive(list1, list2.next)
            return list2


if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(4)

    l2 = ListNode(5)
    l2.next = ListNode(15)
    l2.next.next = ListNode(10)

    l3 = solution.mergeTwoLists(l1, l2)

    while True:
        print(l3.val)
        l3 = l3.next
        if l3 is None:
            break
