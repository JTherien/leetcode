import unittest
from longest_substring_without_repeating_characters import Solution

class exampleCases(unittest.TestCase):

    def test_example_one(self):

        solution = Solution()

        self.assertEqual(solution.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_example_two(self):

        solution = Solution()

        self.assertEqual(solution.lengthOfLongestSubstring("bbbbb"), 1)

    def test_example_three(self):

        solution = Solution()

        self.assertEqual(solution.lengthOfLongestSubstring("pwwkew"), 3)

    def test_example_four(self):

        solution = Solution()

        self.assertEqual(solution.lengthOfLongestSubstring(""), 0)

    def test_example_five(self):

        solution = Solution()

        self.assertEqual(solution.lengthOfLongestSubstring(" "), 1)

    def test_large_string(self):

        solution = Solution()

        with open('longest_substring_without_repeating_characters_example_six.txt', 'r') as file:

            data = file.read()

            self.assertEqual(solution.lengthOfLongestSubstring(data), 95)