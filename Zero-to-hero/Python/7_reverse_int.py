# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

#  

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21



class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        res = ''
        for i in range(len(s)-1, -1, -1):
            res += s[i]
        if x < 0:
            res = '-'+ res[:len(res)-1]
            return int(res) if int(res) >= -pow(2, 31) else 0
        else:
            return int(res) if int(res) <= pow(2, 31)-1 else 0
        
print(Solution().reverse(-1234567))