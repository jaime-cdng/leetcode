"""
26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element
 appears only once. The relative order of the elements should be kept the same. Then return the number of unique
 elements in nums.
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums[:] = sorted(set(nums))
        return len(nums)


if __name__ == "__main__":
    solution = Solution()

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected_nums = [0, 1, 2, 3, 4]

    k = solution.removeDuplicates(nums)

    assert k == len(expected_nums)

    for i in range(k):
        assert nums[i] == expected_nums[i]
