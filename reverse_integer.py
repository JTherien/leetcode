
"""
Given a signed 32-bit integer x, return x with its digits reversed. If 
reversing x causes the value to go outside the signed 32-bit integer 
range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers 
(signed or unsigned).
"""
from math import log10

class Solution:
    
    def reverse(self, x: int) -> int:

        abs_x = abs(x)

        if x == 0:
            
            return 0

        elif abs_x < 10:

            return x

        sign = -1 if x < 0 else 1

        magnitude = int(log10(abs_x))

        num_in = abs_x
        num_out = 0
        
        # Generate an indexed list ranging from 0 to the magnitude of x
        for n in enumerate(range(magnitude, -1, -1)):

            original_mag = (10 ** n[1])
            reversed_mag = (10 ** n[0])

            # Using the list index, find the number's new "position"
            original_mag_num = int(num_in / original_mag) * original_mag
            reversed_mag_num = original_mag_num / original_mag * reversed_mag

            num_in -= original_mag_num
            num_out += reversed_mag_num
                            
        if int(num_out).bit_length()>31:
            
            return 0
        
        else:
            
            return int(sign * num_out)