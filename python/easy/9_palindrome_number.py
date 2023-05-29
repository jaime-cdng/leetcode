"""
9. Palindrome Number

Given an integer x, return true if x is a
palindrome, and false otherwise.
"""

import random


class Solution:
    """
    Solution to the problem 2. Palindrome number.
    """

    def isPalindrome(self, number: int) -> bool:  # With string conversion
        """
        Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as.
        :param number: Number to check.
        :return: True if the number is a palindrome, False otherwise.
        """

        return str(number) == str(number)[::-1]

    def isPalindromeWithouStringConversion(self, number: int) -> bool:  # Without string conversion
        """
        Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as.

        :param number: Number to check.
        :return: True if the number is a palindrome, False otherwise.
        """

        if number < 0:
            return False

        reversed_number = 0

        original_number = number

        while number > 0:
            reversed_number = reversed_number * 10 + number % 10
            print(reversed_number)
            number //= 10
            print(number)
            print("----")

        return reversed_number == original_number


if __name__ == "__main__":
    solution = Solution()
    randon_int = random.randint(1, 1000)
    # print(randon_int)
    # print(solution.isPalindrome(randon_int))
    print(solution.isPalindromeWithouStringConversion(101))
