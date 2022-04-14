# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# Example 1:  Input: x = 123
# Output: 321
# Example 2:  Input: x = -123
# Output: -321

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rem = 0
        neg = 0
        while x != 0:
            #Check if the integer is negetive, remove the - if it is
            if x < 0:
                x = abs(x)
                neg += 1
            #Get last digit of the integer
            n = x % 10
            #Put that digit to the front
            newrem = rem * 10 + n
            # Check overflow 
            if abs(rem) > 0x7FFFFFFF:
                return 0
            if (newrem-n)/10 != rem:
                return 0
            rem = newrem
            x = x/10
        if neg > 0:
            return -rem
        return rem