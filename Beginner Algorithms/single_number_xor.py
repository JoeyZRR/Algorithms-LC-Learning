# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# Example: Input: nums = [2,2,1] Output: 1; Input: nums = [4,1,2,1,2] Output: 4
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Using XOR operator ^
        # 0 ^ k = k
        # k ^ k = 0
        result = 0
        for i in nums:
            result = result ^ i
        return result
