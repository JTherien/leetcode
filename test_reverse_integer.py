import unittest
from reverse_integer import Solution

class exampleCases(unittest.TestCase):

    def test(self):
        
        solution = Solution()
        self.assertEqual(solution.reverse(123), 321)

    def test_negative(self):
        
        solution = Solution()
        self.assertEqual(solution.reverse(-123), -321)

    def test_leading_zero(self):
        
        solution = Solution()
        self.assertEqual(solution.reverse(120), 21)

    def test_zero(self):

        solution = Solution()
        self.assertEqual(solution.reverse(0), 0)

if __name__ == '__main__':
    unittest.main()