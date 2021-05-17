"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. 
For example, 121 is palindrome while 123 is not.

This code does not convert the input integer into a string
"""

from math import log10

class Solution:
    
    def isPalindrome(self, x: int) -> bool:
        
        # Any single digit number non-negative is automatically a palindrome
        if (x < 10) and (x >= 0):
    
            return True

        # Any number less than zero or ends with zero are immediately
        # disqualified as palindromes
        elif (x < 0) or (x % 10 == 0):
            
            return False
        
        magnitude = int(log10(x))
        num_in = x
        num_out = 0

        for n in enumerate(range(magnitude, -1, -1)):

            original_mag = (10 ** n[1])
            reversed_mag = (10 ** n[0])

            # Using the list index, find the number's new "position"
            original_mag_num = int(num_in - (num_in % original_mag))
            reversed_mag_num = original_mag_num / original_mag * reversed_mag

            num_in -= original_mag_num
            num_out += reversed_mag_num

        return x == int(num_out)
