"""
1. Two sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

import random


def random_positive_integers(n, max_value=10) -> list[int]:
    """
    Generate a list of n random positive integers.

    :param n: Number of integers to generate
    :param max_value: Maximum value of the integers
    :return: A list of n random positive integers
    """
    return [random.randint(1, max_value) for _ in range(n)]


class Solution:
    """
    Solution to the problem 1. Two sum.
    """

    def tow_sum(self, nums, target) -> tuple[int, int] or None:
        """
        Find the indices of two numbers in a list that sum to a target value.

        :param nums: List of numbers
        :param target: Number to sum to
        :return: A tuple of the indices of the two numbers that sum to the target value
        """
        number_index = {}  # key: number, value: index

        for index, number in enumerate(nums):
            difference = target - number

            if difference in number_index.keys():
                return number_index[difference], index

            number_index[number] = index


if __name__ == "__main__":
    solution = Solution()
    nums = random_positive_integers(100, 20)
    target = random.randint(1, 20)
    print(nums)
    print(solution.tow_sum(nums, target))
