"""
13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""


class Solution:
    """
    Solution to the problem 13. Roman to Integer.
    """

    def romanToInt(self, roman_number: str) -> int:
        """
        Convert a Roman number to an integer.

        :param roman_number: Roman number to convert.
        :return: Integer representation of the Roman number.
        """

        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        integer = 0

        for index, roman_digit in enumerate(roman_number):
            if index + 1 < len(roman_number) and roman_to_int[roman_digit] < roman_to_int[roman_number[index + 1]]:
                integer -= roman_to_int[roman_digit]
            else:
                integer += roman_to_int[roman_digit]

        return integer


if __name__ == '__main__':
    solution = Solution()
    print(solution.romanToInt('VX'))
    print(solution.romanToInt('III'))
    print(solution.romanToInt('IV'))
    print(solution.romanToInt('IX'))
    print(solution.romanToInt('LVIII'))
    print(solution.romanToInt('MCMXCIV'))
