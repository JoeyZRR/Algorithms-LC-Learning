# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.
# Input: digits = [1,2,3] Output: [1,2,4] Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
import math

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Loop through the list reversely
        for i in range(len(digits)-1, -1, -1):
            # If the digit not 9, simply plus 1 to that digit and return the result
            if digits[i] != 9:
                digits[i] += 1
                return digits
            # If the digit is 9, set it to 0 and keep looping
            else:
                digits[i] = 0
        #Case that all digits are 9, add 1 to the beginning of the list
        digits.insert(0,1)
        return digits
    
math.factorial()