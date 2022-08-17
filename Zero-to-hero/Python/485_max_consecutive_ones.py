# Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                left += 1
                if left > max:
                    max = left
            else:
                left = 0
        return max