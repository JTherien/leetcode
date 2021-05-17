from logging import StrFormatStyle
import unittest
from palindrome_number import Solution

class exampleCases(unittest.TestCase):

    def test(self):
            
        solution = Solution()
        self.assertEqual(solution.isPalindrome(121), True)

    def test_negative_number(self):

        solution = Solution()
        self.assertEqual(solution.isPalindrome(-121), False)

    def test_leading_zero(self):

        solution = Solution()
        self.assertEqual(solution.isPalindrome(10), False)

    def test_single_digit(self):
        
        solution = Solution()
        self.assertEqual(solution.isPalindrome(5), True)

    def test_zero(self):
        
        solution = Solution()
        self.assertEqual(solution.isPalindrome(0), True)              

if __name__ == '__main__':
    unittest.main()