import unittest
from longest_common_prefix import Solution

class exampleCases(unittest.TestCase):

    def test_one(self):

        solution = Solution()
        
        self.assertEqual(solution.longestCommonPrefix(["flower","flow","flight"]), 'fl')

    def test_two(self):

        solution = Solution()
        
        self.assertEqual(solution.longestCommonPrefix(["dog","racecar","car"]), '')