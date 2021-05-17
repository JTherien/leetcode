import unittest
from two_sum import Solution

class exampleCases(unittest.TestCase):

    def test_lists(self):
        
        """
        Test the output when given the following lists:
        nums = [2,7,11,15], target = 9
        nums = [3,2,4], target = 6
        nums = [3,3], target = 6
        """
        
        test_one = Solution.twoSum([2,7,11,15], 9)
        test_two = Solution.twoSum([3,2,4], 6)
        test_three = Solution.twoSum([3,3], 6)

        test_one.sort()
        test_two.sort()
        test_three.sort()

        self.assertEqual(test_one, [0,1])
        self.assertEqual(test_two, [1,2])
        self.assertEqual(test_three, [0,1])

if __name__ == '__main__':
    unittest.main()