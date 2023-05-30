"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order. # ops!
Every close bracket has a corresponding open bracket of the same type.
"""


class Solution(object):
    valid_chars = ["(", ")", "{", "}", "[", "]"]

    def isValid(self, string):
        """
        :type string: str
        :rtype: bool
        """

        if not set(string).issubset(self.valid_chars) or len(string) % 2 != 0:
            return False

        closing_opening = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        lifo = []
        for char in string:
            if char in closing_opening.values():
                lifo.append(char)
            elif char in closing_opening.keys():
                if len(lifo) == 0 or lifo.pop() != closing_opening[char]:
                    return False

        return len(lifo) == 0


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        # "()",
        # "()[]{}",
        # "(]",
        # "([)]",
        # "{[]}",
        "(()[()])"
    ]

    for case in test_cases:
        print(solution.isValid(case))
