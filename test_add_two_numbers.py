from logging import StrFormatStyle
import unittest
from add_two_numbers import Solution
from add_two_numbers import ListNode

class exampleCases(unittest.TestCase):

    def test_example_one(self):
        
        node = ListNode()
        solution = Solution()

        l1 = [2,4,3]
        l2 = [5,6,4]
        l3 = [7,0,8]
        
        self.assertEqual(solution.addTwoNumbers(l1, l2), l3)

    def test_example_two(self):
        
        node = ListNode()
        solution = Solution()

        l1 = [0]
        l2 = [0]
        l3 = [0]
        
        self.assertEqual(solution.addTwoNumbers(l1, l2), l3)


    def test_example_three(self):
        
        node = ListNode()
        solution = Solution()

        l1 = [9,9,9,9,9,9,9]
        l2 = [9,9,9,9]
        l3 = [8,9,9,9,0,0,0,1]

        self.assertEqual(solution.addTwoNumbers(l1, l2), l3)
