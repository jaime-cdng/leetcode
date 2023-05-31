"""
28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle
is not part of haystack.
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if needle not in haystack:
            return -1

        return haystack.index(needle)


if __name__ == "__main__":
    solution = Solution()
    print(solution.strStr("Problem28", "28"))
    print(solution.strStr("Problem28", "29"))
