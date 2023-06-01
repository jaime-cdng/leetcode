"""
27. Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the
elements may be changed. Then return the number of elements in nums which are not equal to val.
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        new = []

        for num in nums:
            if num != val:
                new.append(num)

        nums[:] = new

        return len(nums)


if __name__ == "__main__":
    solution = Solution()

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2

    print(solution.removeElement(nums, val))
