import unittest
from valid_parentheses import Solution

class exampleCases(unittest.TestCase):

    def test_one(self):

        solution = Solution()
        
        self.assertEqual(solution.isValid("()"), True)

    def test_two(self):

        solution = Solution()
        
        self.assertEqual(solution.isValid("()[]{}"), True)

    def test_three(self):

        solution = Solution()
        
        self.assertEqual(solution.isValid("(]"), False)

    def test_four(self):

        solution = Solution()
        
        self.assertEqual(solution.isValid("([)]"), False)

    def test_five(self):
        
        solution = Solution()
        
        self.assertEqual(solution.isValid("{[]}"), True)