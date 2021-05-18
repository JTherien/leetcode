import unittest
from roman_to_integer import Solution

class exampleCases(unittest.TestCase):

    def test_three(self):
        
        solution = Solution()
        self.assertEqual(solution.romanToInt("III"), 3)

    def test_four(self):
        
        solution = Solution()
        self.assertEqual(solution.romanToInt("IV"), 4)

    def test_fifty_eight(self):

        solution = Solution()
        self.assertEqual(solution.romanToInt("LVIII"), 58)

    def test_nineteen_ninety_four(self):

        solution = Solution()
        self.assertEqual(solution.romanToInt("MCMXCIV"), 1994)

if __name__ == '__main__':
    unittest.main()