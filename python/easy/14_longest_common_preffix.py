"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


class SuboptimalSolution(object):
    def longestCommonPrefix(self, str_list: list[str]):
        """
        :type str_list: List[str]
        :rtype: str
        """

        if not str_list:
            return ""

        common_prefix: str = min(str_list, key=len)

        while len(common_prefix) > 0:
            for string in str_list:
                if not string.startswith(common_prefix):
                    common_prefix = common_prefix[:len(common_prefix) - 1]
                    continue

                if all(s.startswith(common_prefix) for s in str_list):
                    return common_prefix

        return ""


class Solution(object):
    def longestCommonPrefix(self, str_list: list[str]):
        """
        :type str_list: List[str]
        :rtype: str
        """

        if not str_list:
            return ""

        common_prefix: str = min(str_list, key=len)

        for i in range(len(common_prefix)):
            if any(string[i] != common_prefix[i] for string in str_list):
                return common_prefix[:i]

        return common_prefix


class AlternativeSolution(object):
    def longestCommonPrefix(self, str_list):
        if not str_list:
            return ""

        str_list.sort()

        first_str = str_list[0]
        last_str = str_list[-1]

        index = 0
        while index < len(first_str) and first_str[index] == last_str[index]:
            index += 1

        return first_str[:index]


if __name__ == "__main__":
    solution = SuboptimalSolution()
    strs = ["a"]
    s = solution.longestCommonPrefix(strs)
    print(s)
