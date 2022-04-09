# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# Example: Input: nums = [2,2,1] Output: 1; Input: nums = [4,1,2,1,2] Output: 4

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Using set to remove duplicate numbers, mutiple sum by 2 because every element appears twice except for one
        #The compair the difference between sum of set*2 and sum of nums will get the nonduplicate number
        return sum(set(nums)) * 2 - sum(nums)
